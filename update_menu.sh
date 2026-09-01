#!/bin/bash
# Quick menu update script
# Usage: ./update_menu.sh

EXCEL_FILE="plantilla-menu-teckels.xlsx"
OUTPUT_FILE="menu-data.js"
SCRIPT="scripts/update_menu.py"

if [ ! -f "$EXCEL_FILE" ]; then
    echo "❌ Error: $EXCEL_FILE not found!"
    exit 1
fi

if [ ! -f "$SCRIPT" ]; then
    echo "❌ Error: $SCRIPT not found!"
    exit 1
fi

echo "🔄 Updating menu from Excel..."
python3 "$SCRIPT" "$EXCEL_FILE" --output "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
    echo "✅ Menu updated successfully!"
    echo "📝 File: $OUTPUT_FILE"
    ls -lh "$OUTPUT_FILE"
else
    echo "❌ Error updating menu!"
    exit 1
fi
