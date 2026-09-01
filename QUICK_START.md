# Teckel's Menu - Quick Start Guide

## ✅ Setup Complete!

Your menu automation is now fully integrated into the GitHub repository.

### 📁 Files in the project:

- **`plantilla-menu-teckels.xlsx`** — Excel file with all menu data (source of truth)
- **`menu-data.js`** — Generated JavaScript file (auto-created, don't edit)
- **`update_menu.sh`** — Quick update script
- **`scripts/update_menu.py`** — Python importer
- **`index.html`** — Main website (loads menu automatically)
- **`menu-qr.html`** — QR menu version (loads menu automatically)
- **`teckels_menu.html`** — Menu page (loads menu automatically)

---

## 🚀 How to Update the Menu

### Quick way (Recommended):

```bash
cd ~/porfolio
./update_menu.sh
git add menu-data.js
git commit -m "Update menu from Excel"
git push
```

### Manual way:

```bash
python3 scripts/update_menu.py plantilla-menu-teckels.xlsx --output menu-data.js
```

---

## 📊 Current Menu Status

✅ **58 items** across **12 categories**
✅ **3 languages**: English, German, Spanish
✅ **Prices in EUR**: 4,90€ - 18,90€
✅ **All items visible**: yes

### Categories:
1. 🥗 Starters (10 items)
2. 🍔 Burgers (3 items)
3. 🍖 Mains (4 items)
4. 🍟 Sides (7 items)
5. 🍫 Desserts (2 items)
6. 🥤 Soft Drinks (5 items)
7. 🍺 Beer (6 items)
8. 🍷 Wine (7 items)
9. 🍹 Sangria (2 items)
10. 🥂 Sekt (4 items)
11. 🍸 Cocktails (6 items)
12. 🥃 Shots (2 items)

---

## ✏️ How to Edit the Menu

1. **Open** `plantilla-menu-teckels.xlsx` in Excel
2. **Edit** items, prices, descriptions
3. **Hide items**: Change `visible` column to `no`
4. **Add items**: Add new rows in the category
5. **Save** the file
6. **Run** `./update_menu.sh`
7. **Push** to GitHub

### Important columns:
- `item_en` / `item_de` / `item_es` — Item names in 3 languages
- `price` — Price in format "X,XX €"
- `visible` — "yes" to show, anything else to hide
- `description_*` — Descriptions in 3 languages

---

## 🌐 Where it appears

All three website versions load the menu automatically:
- https://github.com/delmardigital/porfolio → `index.html`
- QR menu → `menu-qr.html`
- Standalone menu → `teckels_menu.html`

When you update the Excel file and run the script, all three websites show the new menu instantly.

---

## 📞 Questions?

Check `README-MENU-UPDATES.md` for detailed documentation.

---

**Last updated**: September 1, 2026
