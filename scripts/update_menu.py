#!/usr/bin/env python3
"""
Teckel's Menu Updater
Converts Excel menu to JavaScript data file for the website.

Usage:
    python3 update_menu.py plantilla-menu-teckels.xlsx --output menu-data.js
    python3 update_menu.py                                    # auto-find Excel
"""

import sys
import json
from pathlib import Path
from openpyxl import load_workbook
import argparse


def clean_text(value):
    """Clean and normalize text from Excel cells."""
    if value is None:
        return ""
    return str(value).strip()


def get_cell(row, col_index, ws):
    """Safely get cell value with bounds checking."""
    try:
        return clean_text(ws.cell(row, col_index).value)
    except:
        return ""


def build_menu(xlsx_path):
    """Parse Excel file and build menu structure."""
    wb = load_workbook(xlsx_path)
    ws = wb['Menu']
    
    menu = []
    current_category = None
    
    # Row 4 has headers, data starts at row 5
    for row in range(5, 200):
        cat_id = get_cell(row, 1, ws)
        if not cat_id:
            break
        
        # Check if this is a new category
        if current_category is None or current_category['id'] != cat_id:
            # Save previous category if exists
            if current_category is not None:
                menu.append(current_category)
            
            # Create new category
            current_category = {
                'id': cat_id,
                'e': get_cell(row, 2, ws),  # emoji
                'name': {
                    'en': get_cell(row, 4, ws),
                    'de': get_cell(row, 5, ws),
                    'es': get_cell(row, 6, ws),
                },
                'sub': {
                    'en': get_cell(row, 7, ws),
                    'de': get_cell(row, 8, ws),
                    'es': get_cell(row, 9, ws),
                },
                'items': []
            }
        
        # Add item to current category
        item_name_en = get_cell(row, 11, ws)
        visible = get_cell(row, 18, ws).lower()
        
        # Only include visible items (yes/true)
        if visible in ['yes', 'true', '1']:
            item = {
                'n': {
                    'en': item_name_en,
                    'de': get_cell(row, 12, ws),
                    'es': get_cell(row, 13, ws),
                },
                'd': {
                    'en': get_cell(row, 14, ws),
                    'de': get_cell(row, 15, ws),
                    'es': get_cell(row, 16, ws),
                },
                'p': get_cell(row, 17, ws),  # price
            }
            current_category['items'].append(item)
    
    # Add last category
    if current_category is not None:
        menu.append(current_category)
    
    return menu


def write_js(menu, output_path):
    """Export menu as JavaScript file."""
    json_str = json.dumps(menu, ensure_ascii=False, indent=2)
    js_content = f"window.TECKELS_MENU = {json_str};"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_content)


def find_xlsx(path_hint=None):
    """Find Excel file in common locations."""
    search_paths = [
        Path('plantilla-menu-teckels.xlsx'),
        Path.home() / 'Desktop' / 'plantilla-menu-teckels.xlsx',
        Path.home() / 'Documents' / 'plantilla-menu-teckels.xlsx',
        Path('/Users/leandrodelmar/Documents/Codex/2026-08-19/ne/outputs/plantilla-menu-teckels.xlsx'),
    ]
    
    if path_hint:
        search_paths.insert(0, Path(path_hint))
    
    for path in search_paths:
        if path.exists():
            return path
    
    return None


def main():
    parser = argparse.ArgumentParser(
        description='Convert Excel menu to JavaScript data file'
    )
    parser.add_argument(
        'xlsx_file',
        nargs='?',
        default=None,
        help='Path to plantilla-menu-teckels.xlsx'
    )
    parser.add_argument(
        '--output',
        default='menu-data.js',
        help='Output JavaScript file (default: menu-data.js)'
    )
    
    args = parser.parse_args()
    
    # Find Excel file
    xlsx_path = find_xlsx(args.xlsx_file)
    
    if not xlsx_path or not xlsx_path.exists():
        print("❌ Error: plantilla-menu-teckels.xlsx not found!")
        print("Please provide the path or place it in the current directory.")
        sys.exit(1)
    
    try:
        # Build menu from Excel
        menu = build_menu(xlsx_path)
        
        # Write JavaScript file
        write_js(menu, args.output)
        
        # Count stats
        categories = len(menu)
        products = sum(len(cat['items']) for cat in menu)
        
        print(f"✅ Menu generated successfully: {args.output}")
        print(f"   Categories: {categories}")
        print(f"   Products: {products}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
