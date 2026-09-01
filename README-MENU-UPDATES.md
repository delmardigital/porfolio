# Teckels Menu Updates

The website now loads the menu from an **external Excel file** instead of hardcoding the data.

## How it works

1. **Excel source of truth**: [`plantilla-menu-teckels.xlsx`](https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID)
   - Contains all menu items in 3 languages (English, German, Spanish)
   - Edit items, prices, descriptions here

2. **Auto-generated data file**: `menu-data.js`
   - Generated from the Excel file
   - Contains all categories and items in JavaScript format
   - Loaded automatically by the website

3. **Website**: `index.html`
   - Loads `menu-data.js` before rendering
   - If the file is missing, it uses a minimal fallback

## To update the menu

### Option 1: From your Mac (Command Line)

```bash
# Generate the menu file from Excel
python3 scripts/update_menu.py /path/to/plantilla-menu-teckels.xlsx --output menu-data.js

# The website now shows the updated menu!
```

### Option 2: Using the provided script

A pre-built Python script is included at: `scripts/update_menu.py`

Usage:
```bash
python3 scripts/update_menu.py [EXCEL_FILE] --output [OUTPUT_JS_FILE]
```

Examples:
```bash
# Auto-find the Excel file
python3 scripts/update_menu.py

# Specify exact paths
python3 scripts/update_menu.py ~/Documents/plantilla-menu-teckels.xlsx --output ./menu-data.js
```

## Menu structure (Excel)

The spreadsheet has these columns:

- `category_id`: Unique ID (e.g., "starters", "burgers")
- `category_icon`: Emoji (e.g., "🥗", "🍔")
- `category_order`: Display order (1, 2, 3...)
- `category_en` / `category_de` / `category_es`: Category names
- `category_description_*`: Optional descriptions
- `item_order`: Order within category
- `item_en` / `item_de` / `item_es`: Item names
- `description_*`: Descriptions in 3 languages
- `price`: Price (e.g., "12,90 €")
- `visible`: "yes" or "no" to hide items

## How to hide an item

Set the `visible` column to `no` for that row, then regenerate the menu file.

## Technical notes

- The website loads `menu-data.js` first
- If it's missing or broken, it falls back to a minimal menu
- You can edit the Excel file and regenerate as often as you need
- No need to touch the HTML file for menu changes

## Files involved

```
index.html              ← Main website (loads menu-data.js automatically)
menu-data.js            ← Generated from Excel (DO NOT edit manually)
scripts/update_menu.py  ← Python script to generate the menu file
plantilla-menu-teckels.xlsx  ← Excel source (edit this!)
```

## Questions?

If the menu doesn't update:
1. Make sure the Excel file has the correct structure
2. Run the Python script again
3. Reload the website in your browser
4. Check the browser console for errors

---

**Last updated**: September 1, 2026
