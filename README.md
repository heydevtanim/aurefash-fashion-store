# AUREFASH

AUREFASH is an independent premium fashion storefront concept and portfolio case study. The repository contains a responsive front-end prototype and an eight-page case-study PDF. It does not connect to a live WordPress installation or process orders.

## Open the storefront

Open `index.html` in a current browser. Product photography and Google Fonts are loaded from external services, so an internet connection is needed for those visual assets. The layout and locally stored SVG identity assets remain available offline.

The prototype includes:

- Responsive editorial homepage, category links, product cards and custom AUREFASH / AF marks.
- Category filtering and product quick-view dialogs.
- Clothing size selection, accessory one-size selection, add/remove bag actions and a locally persisted demo subtotal.
- A demo checkout notice and newsletter notice that clearly explain that no transaction or email signup takes place.
- Custom reusable SVG logo and interface icons in `assets/`.

The sample catalogue, prices, product descriptions, shipping threshold and editorial copy are fictional portfolio content. Replace these with approved business information before commercial use. Product photos are hosted by Unsplash and must be replaced with images that are licensed for the intended use.

## Case study

`AUREFASH-Portfolio-Case-Study.pdf` covers the brand concept, color and type system, storefront journey, proposed WordPress/WooCommerce architecture, responsive/accessibility considerations, implementation phases, QA checklist and honest portfolio copy. It distinguishes prototype behavior from production functionality and measured outcomes.

`build_case_study.py` generates the PDF with Python and ReportLab. Install the dependency, then rebuild:

```powershell
python -m pip install -r requirements.txt
python build_case_study.py
```

## Suggested WordPress / WooCommerce implementation

1. Create a local or staging WordPress environment and install a supported WooCommerce version.
2. Implement the brand tokens and templates as a custom block theme or a child theme. Keep the static prototype as a visual reference, not as a replacement for WooCommerce commerce logic.
3. Create real products, attributes, sizes, colors, stock rules, tax and shipping settings. Use native WooCommerce cart and checkout validation.
4. Configure HTTPS, a supported payment provider in test mode, transactional email, least-privilege accounts, backup and restoration.
5. Run the QA matrix in the PDF on the deployed staging site. Save dated evidence and replace concept claims with verified implementation details.

## Files

- `index.html` — storefront structure
- `styles.css` — responsive visual system
- `app.js` — catalogue, filters, product dialog and local demo bag
- `assets/` — custom SVG marks and interface icons
- `build_case_study.py` — editable PDF generator
- `AUREFASH-Portfolio-Case-Study.pdf` — portfolio handoff document
