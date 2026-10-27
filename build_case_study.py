"""Build the AUREFASH portfolio case-study PDF."""
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Flowable)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'AUREFASH-Portfolio-Case-Study.pdf'
INK=HexColor('#171717'); IVORY=HexColor('#F5F1E8'); GOLD=HexColor('#B69A6A')
STONE=HexColor('#E5E0D7'); TAUPE=HexColor('#68645E'); WHITE=colors.white; PALE=HexColor('#ECE7DD')
PAGE_W,PAGE_H=A4
try:
    pdfmetrics.registerFont(TTFont('DM','C:/Windows/Fonts/arial.ttf'))
    pdfmetrics.registerFont(TTFont('DM-Bold','C:/Windows/Fonts/arialbd.ttf'))
    pdfmetrics.registerFont(TTFont('Display','C:/Windows/Fonts/georgia.ttf'))
    pdfmetrics.registerFont(TTFont('Display-Italic','C:/Windows/Fonts/georgiai.ttf'))
except Exception:
    pass
SANS='DM'; SANS_B='DM-Bold'; SERIF='Display'; SERIF_I='Display-Italic'

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='eyebrow',fontName=SANS_B,fontSize=7.5,leading=10,textColor=TAUPE,spaceAfter=7,tracking=1.5))
styles.add(ParagraphStyle(name='h1x',fontName=SERIF,fontSize=30,leading=34,textColor=INK,spaceAfter=13))
styles.add(ParagraphStyle(name='h2x',fontName=SERIF,fontSize=18,leading=22,textColor=INK,spaceBefore=8,spaceAfter=8))
styles.add(ParagraphStyle(name='h3x',fontName=SANS_B,fontSize=9,leading=13,textColor=INK,spaceBefore=5,spaceAfter=4))
styles.add(ParagraphStyle(name='bodyx',fontName=SANS,fontSize=9,leading=14,textColor=TAUPE,spaceAfter=7))
styles.add(ParagraphStyle(name='smallx',fontName=SANS,fontSize=7.4,leading=10,textColor=TAUPE,spaceAfter=3))
styles.add(ParagraphStyle(name='whitebody',fontName=SANS,fontSize=9,leading=14,textColor=WHITE))
styles.add(ParagraphStyle(name='tablehead',fontName=SANS_B,fontSize=7.4,leading=10,textColor=WHITE))
styles.add(ParagraphStyle(name='tablecell',fontName=SANS,fontSize=7.5,leading=10.3,textColor=INK))
styles.add(ParagraphStyle(name='cover-title',fontName=SERIF,fontSize=41,leading=44,textColor=INK))
styles.add(ParagraphStyle(name='quote',fontName=SERIF_I,fontSize=20,leading=28,textColor=INK,alignment=TA_CENTER))

def P(txt,style='bodyx'): return Paragraph(txt,styles[style])
def bullets(items):
    return [P('<font color="#B69A6A">●</font>&nbsp;&nbsp;'+x,'bodyx') for x in items]

class SwatchRow(Flowable):
    def __init__(self): super().__init__(); self.height=50
    def wrap(self,w,h): self.width=w; return w,self.height
    def draw(self):
        names=[('Obsidian','#171717'),('Warm ivory','#F5F1E8'),('Champagne','#B69A6A'),('Soft stone','#E5E0D7'),('Slate taupe','#68645E')]
        gap=8; cell=(self.width-gap*4)/5
        for i,(n,hx) in enumerate(names):
            x=i*(cell+gap); self.canv.setFillColor(HexColor(hx)); self.canv.roundRect(x,20,cell,24,3,fill=1,stroke=0)
            self.canv.setFont(SANS_B,6.3); self.canv.setFillColor(INK); self.canv.drawString(x,10,n)
            self.canv.setFont(SANS,6.2); self.canv.setFillColor(TAUPE); self.canv.drawString(x,1,hx)

class MiniStore(Flowable):
    def __init__(self): super().__init__(); self.height=205
    def wrap(self,w,h): self.width=w; return w,self.height
    def draw(self):
        c=self.canv; w=self.width; c.setFillColor(WHITE); c.roundRect(0,0,w,self.height,5,fill=1,stroke=0)
        c.setFillColor(INK); c.rect(0,self.height-20,w,20,fill=1,stroke=0)
        c.setFillColor(HexColor('#eee8dc')); c.setFont(SANS,6.4); c.drawCentredString(w/2,self.height-13,'COMPLIMENTARY SHIPPING ON ORDERS OVER $150')
        c.setFillColor(IVORY); c.rect(0,self.height-49,w,29,fill=1,stroke=0)
        c.setFillColor(TAUPE); c.setFont(SANS,6.5); c.drawString(12,self.height-37,'NEW ARRIVALS     WOMEN     ACCESSORIES')
        c.setFillColor(INK); c.setFont(SERIF,9); c.drawCentredString(w/2,self.height-37,'A U R E F A S H')
        c.setFillColor(HexColor('#817565')); c.rect(0,45,w,self.height-94,fill=1,stroke=0)
        c.setFillColor(HexColor('#5c5348')); c.rect(0,45,w*.49,self.height-94,fill=1,stroke=0)
        c.setFillColor(WHITE); c.setFont(SANS_B,6.5); c.drawString(16,self.height-72,'THE NEW SEASON EDIT')
        c.setFont(SERIF,24); c.drawString(15,self.height-101,'Dress for')
        c.setFont(SERIF_I,24); c.drawString(15,self.height-126,'your own')
        c.setFont(SERIF,24); c.drawString(15,self.height-151,'rhythm.')
        c.setFillColor(WHITE); c.roundRect(15,59,112,18,2,fill=1,stroke=0)
        c.setFillColor(INK); c.setFont(SANS_B,5.7); c.drawString(24,66,'EXPLORE THE COLLECTION  →')
        c.setFillColor(GOLD); c.circle(w*.76,105,39,fill=1,stroke=0); c.setFillColor(HexColor('#d8c4a5')); c.circle(w*.76,105,27,fill=1,stroke=0)
        c.setFillColor(INK); c.setFont(SANS,6); c.drawCentredString(w/2,25,'COLLECTIONS     /     EDITORIAL     /     MADE TO BE WORN')

def page_art(c,doc):
    n=doc.page
    if n==1:
        c.setFillColor(IVORY); c.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
        c.setFillColor(INK); c.rect(PAGE_W*0.57,0,PAGE_W*.43,PAGE_H,fill=1,stroke=0)
        c.setFillColor(HexColor('#62594d')); c.rect(PAGE_W*.57,0,PAGE_W*.43,PAGE_H*.83,fill=1,stroke=0)
        c.setFillColor(HexColor('#b6a48a')); c.ellipse(PAGE_W*.65,PAGE_H*.28,PAGE_W*.94,PAGE_H*.79,fill=1,stroke=0)
        c.setFillColor(HexColor('#302c29')); c.saveState(); c.translate(PAGE_W*.78,PAGE_H*.45); c.rotate(-8); c.roundRect(-44,-108,88,224,32,fill=1,stroke=0); c.restoreState()
        c.setFillColor(GOLD); c.circle(PAGE_W*.79,PAGE_H*.84,8,fill=1,stroke=0)
        c.setFillColor(INK); c.setFont(SANS_B,7); c.drawString(22*mm,PAGE_H-22*mm,'A U R E F A S H')
        c.setFillColor(TAUPE); c.setFont(SANS,7); c.drawString(22*mm,PAGE_H-29*mm,'BRAND & DIGITAL STOREFRONT CONCEPT')
        c.setFillColor(INK); c.setFont(SERIF,37); c.drawString(22*mm,PAGE_H*.57,'A quieter')
        c.setFont(SERIF_I,39); c.drawString(22*mm,PAGE_H*.49,'kind of')
        c.setFont(SERIF,37); c.drawString(22*mm,PAGE_H*.415,'statement.')
        c.setStrokeColor(GOLD); c.setLineWidth(1); c.line(22*mm,PAGE_H*.37,66*mm,PAGE_H*.37)
        c.setFillColor(TAUPE); c.setFont(SANS,10); c.drawString(22*mm,PAGE_H*.33,'A considered fashion store concept')
        c.drawString(22*mm,PAGE_H*.30,'for modern everyday dressing.')
        c.setFillColor(INK); c.setFont(SANS_B,7); c.drawString(22*mm,27*mm,'PORTFOLIO CASE STUDY   ·   2026')
        c.setFillColor(HexColor('#efe9de')); c.setFont(SANS,7); c.drawString(PAGE_W*.61,20*mm,'AUREFASH    /    SPRING–SUMMER EDIT')
        return
    c.setFillColor(IVORY); c.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
    c.setFillColor(TAUPE); c.setFont(SANS_B,6.5); c.drawString(19*mm,PAGE_H-14*mm,'AUREFASH   /   PORTFOLIO CASE STUDY')
    c.setStrokeColor(STONE); c.setLineWidth(.5); c.line(19*mm,PAGE_H-17*mm,PAGE_W-19*mm,PAGE_H-17*mm)
    c.line(19*mm,15*mm,PAGE_W-19*mm,15*mm)
    c.setFont(SANS,6.5); c.setFillColor(TAUPE); c.drawString(19*mm,10*mm,'BRAND CONCEPT  ·  WORDPRESS + WOOCOMMERCE')
    c.drawRightString(PAGE_W-19*mm,10*mm,f'{n:02d}')

class CaseDoc(BaseDocTemplate):
    def __init__(self,path):
        super().__init__(path,pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,topMargin=24*mm,bottomMargin=21*mm,title='AUREFASH — Portfolio Case Study',author='AUREFASH Studio')
        self.addPageTemplates(PageTemplate(id='main',frames=[Frame(self.leftMargin,self.bottomMargin,self.width,self.height,id='normal')],onPage=page_art))

def table(data,widths,header=True):
    converted=[]
    for ri,row in enumerate(data):
        converted.append([P(str(x),'tablehead' if header and ri==0 else 'tablecell') for x in row])
    t=Table(converted,colWidths=widths,repeatRows=1 if header else 0,hAlign='LEFT')
    commands=[('GRID',(0,0),(-1,-1),.45,STONE),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]
    if header: commands += [('BACKGROUND',(0,0),(-1,0),INK),('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE,PALE])]
    t.setStyle(TableStyle(commands)); return t

story=[]
# 1 Cover
story += [Spacer(1,1),PageBreak()]
# 2 Overview
story += [P('01  /  THE PROJECT','eyebrow'),P('A considered place to shop.','h1x'),P('AUREFASH is a premium fashion and lifestyle storefront concept built around the pieces people reach for most. The experience pairs a restrained editorial identity with familiar, practical shopping patterns: browse a collection, understand the product, choose a variation and review a clear bag.','bodyx'),Spacer(1,4*mm)]
story += [table([['PROJECT','ROLE','PLATFORM','STATUS'],['Fashion e-commerce','WordPress & WooCommerce developer','WordPress · WooCommerce','Portfolio concept / prototype']], [35*mm,47*mm,44*mm,44*mm])]
story += [P('The brief','h2x'),P('Create a distinctive, responsive fashion store with an ivory-and-obsidian visual language, a custom wordmark and a shopping flow that remains straightforward on mobile. The project is presented as a concept prototype; no live store, sales data, customer reviews or production payment service is claimed.','bodyx'),P('Design principles','h2x')]
principles=[["01  Considered" ,"A compact edit and visual hierarchy let the products lead."],["02  Clear","Prices, product details and next steps stay easy to scan."],["03  Comfortable","Generous spacing, calm color and responsive layouts support unhurried browsing."],["04  Credible","Only verified business information belongs in a real launch." ]]
story += [table([['PRINCIPLE','EXPERIENCE DECISION']]+principles,[42*mm,128*mm])]
story += [PageBreak()]
# 3 brand
story += [P('02  /  BRAND IDENTITY','eyebrow'),P('A quiet signature.','h1x'),P('The visual identity uses a refined uppercase wordmark and a custom AF monogram. A fine circular frame and champagne line give the monogram a distinctive stamp for the favicon, social avatar, and small brand touchpoints. The identity is intentionally legible in one color and at compact sizes.','bodyx'),Spacer(1,4*mm),SwatchRow(),P('Color with a clear job','h2x'),table([['COLOR','HEX','ROLE'],['Obsidian black','#171717','Navigation, typography, footer and primary actions'],['Warm ivory','#F5F1E8','Main canvas and editorial breathing room'],['Muted champagne gold','#B69A6A','Small marks, subtle emphasis and interactive hover'],['Soft stone','#E5E0D7','Borders, quiet surfaces and dividers'],['Slate taupe','#68645E','Secondary copy and product metadata'],['White','#FFFFFF','Product imagery surface and contrast']], [42*mm,34*mm,94*mm]),P('Type & imagery','h2x'),P('Playfair Display gives headings an editorial voice; DM Sans keeps navigation, controls and product details crisp. The photography direction favors natural light, tactile surfaces, neutral styling and a consistent crop. The prototype uses image references hosted by Unsplash; replace them with licensed, brand-approved product photography before a commercial launch.','bodyx'),P('Palette note: champagne is an accent and hover state, never the default primary button color. Keep large copy in black or taupe for legibility.','smallx'),PageBreak()]
# 4 Storefront experience
story += [P('03  /  STOREFRONT EXPERIENCE','eyebrow'),P('An editorial entry. A familiar path.','h1x'),P('The home page introduces the season, then moves from a small new-arrival edit into category discovery and a broader product grid. A story section gives the concept a human point of view; a restrained newsletter sign-up and service links close the page.','bodyx'),Spacer(1,3*mm),MiniStore(),Spacer(1,4*mm),table([['PAGE / MOMENT','PURPOSE','KEY CONTENT'],['Home','Introduce the brand and lead into shopping','Season edit, new arrivals, categories, story'],['Collection','Help shoppers narrow the edit','Category filters and consistent product cards'],['Product detail','Support an informed choice','Image, price, color, size, description, add to bag'],['Bag','Make the selection easy to review','Line items, remove action and subtotal'],['Checkout handoff','Explain the next step honestly','Demo notice; live WooCommerce connection required']], [34*mm,55*mm,81*mm]),P('Primary journey','h2x'),P('Home → collection → product detail → choose options → bag → checkout. Clear headings, persistent bag count, price visibility and mobile-first controls reduce guesswork at each step. The current prototype does not charge a payment method, calculate shipping or submit an order.','bodyx'),PageBreak()]
# 5 functions + technical scope
story += [P('04  /  FUNCTION & BUILD PLAN','eyebrow'),P('A useful prototype, ready to extend.','h1x'),P('The static storefront demonstrates the visual system and front-end interactions. A production WordPress build would map those patterns to a maintainable theme and WooCommerce data, preserving the platform’s native stock, variation, cart and order rules.','bodyx'),table([['AREA','PROTOTYPE NOW','PRODUCTION IMPLEMENTATION'],['Brand UI','Responsive editorial storefront','Reusable WordPress theme templates and design tokens'],['Catalogue','Eight sample product cards and category filters','Real catalogue, taxonomies, attributes, SKU and stock'],['Product detail','Quick view, options and add-to-bag interaction','WooCommerce variable product with validated availability'],['Bag','Browser-local demo bag and subtotal','WooCommerce session cart, shipping and tax rules'],['Checkout','Clear prototype notice','Gateway, HTTPS, validation, order confirmation and emails'],['Newsletter','Consent-free visual form demo','Configured provider, consent copy and privacy handling']], [29*mm,60*mm,81*mm]),P('Suggested technical stack','h2x'),P('<b>CMS / commerce</b>  WordPress + WooCommerce<br/><b>Theme layer</b>  Custom block theme or child theme; PHP templates and theme.json tokens<br/><b>Front end</b>  HTML, CSS and JavaScript; progressive enhancement and responsive layouts<br/><b>Data</b>  WooCommerce product, attribute, stock, order and customer models on MySQL<br/><b>Operations</b>  Managed hosting, HTTPS, updates, backups, transactional email and a supported payment gateway','bodyx'),P('For the portfolio, label code as a static visual prototype unless a WordPress instance and the listed commerce paths have actually been configured.','smallx'),PageBreak()]
# 6 responsive + accessibility
story += [P('05  /  RESPONSIVE DESIGN & ACCESSIBILITY','eyebrow'),P('Quiet on desktop. Clear on mobile.','h1x'),P('The layout is designed to adapt from a wide editorial header and four-column product grid to a compact menu and two-column grid. Product detail, bag and navigation controls have explicit labels; imagery includes descriptive alt text; the palette reserves contrast for functional text and actions.','bodyx'),table([['VIEWPORT','LAYOUT BEHAVIOR','REVIEW POINTS'],['Wide desktop  1280+','Full navigation, four product columns, split editorial story','Visual balance, image crop, long product names'],['Tablet  621–850','Condensed navigation and fluid card widths','No overlap at intermediate widths'],['Mobile  up to 620','Menu toggle, two product columns, stacked story and forms','Touch target size, horizontal overflow, dialog scrolling']], [37*mm,68*mm,65*mm]),P('Accessibility checks before launch','h2x')]+bullets(['Keyboard reachability and visible focus for every interactive control.','Dialog focus entry, Escape dismissal and focus return; announce bag changes to assistive technology.','WCAG contrast checks for taupe text, gold hover states and labels on imagery.','Respect reduced-motion preference and avoid conveying product availability by color alone.','Validate semantic headings, form labels, error messages and zoom at 200%.'])+[P('The prototype is a visual starting point. Accessibility conformance must be verified against the final theme, content, plugins and checkout.','smallx'),PageBreak()]
# 7 process + QA
story += [P('06  /  DELIVERY PROCESS & QA','eyebrow'),P('Build with evidence at every step.','h1x'),table([['PHASE','WORK','OUTPUT'],['01  Discovery','Confirm audience, catalogue, fulfilment rules and brand references','Approved scope and site map'],['02  Design','Establish tokens, page hierarchy, responsive patterns and product photography','Screen designs and interaction states'],['03  Build','Implement theme, WooCommerce products, variation rules and templates','Working staging store'],['04  Verify','Exercise responsive, commerce, accessibility, performance and SEO checks','QA record and defect fixes'],['05  Launch','Harden access, configure payments, backups, email and monitoring','Release checklist and recovery path']], [34*mm,84*mm,52*mm]),P('Pre-launch QA checklist','h2x'),table([['CHECK','PASS CONDITION','EVIDENCE TO SAVE'],['Responsive pages','Home, collection, product, bag and checkout work at target sizes','Viewport captures and issue log'],['Variation & stock','Each size/color combination shows correct price and availability','Test product matrix'],['Bag totals','Add/remove/update recalculates items, shipping, tax and total','Cart test record'],['Checkout','Required-field, address, payment success/failure and cancellation paths behave correctly','Gateway test-mode order IDs'],['Order operations','Correct customer, line items, status and email are recorded','Redacted order/admin screenshots'],['Accessibility','Keyboard, screen reader basics, contrast, labels and error states reviewed','Audit notes and fixes'],['Performance & SEO','Measure representative pages; inspect metadata, sitemap and indexability','Named tool, date, URL and result'],['Security & recovery','HTTPS, least privilege, updates, backup and restore tested','Configuration and restore record']], [32*mm,83*mm,55*mm]),P('Record results with the test date, device/browser, method and observed value. Do not substitute expected outcomes for measured results.','smallx'),PageBreak()]
# 8 portfolio publication
story += [P('07  /  PORTFOLIO HANDOFF','eyebrow'),P('Describe the work honestly.','h1x'),P('This case study is ready to accompany the visual prototype. When the project is implemented in WordPress, replace concept language with the verified work, capture real screens, and add only measured results.','bodyx'),P('Portfolio title','h2x'),P('AUREFASH — Premium Fashion E-commerce Store Concept','h3x'),P('Short description','h2x'),P('Designed a premium fashion storefront concept for WordPress and WooCommerce, with a custom visual identity, responsive editorial homepage and a clear product discovery and shopping journey. The prototype demonstrates category filtering, product quick views and a browser-local bag.','bodyx'),P('Suggested project facts','h2x'),table([['FIELD','PORTFOLIO COPY'],['Role','WordPress & WooCommerce Developer (update to match your actual contribution)'],['Project type','Independent portfolio concept'],['Status','Responsive front-end prototype; WooCommerce integration pending'],['Tools','HTML, CSS, JavaScript prototype; planned WordPress + WooCommerce'],['Verified result','Add only after implementation and documented testing']], [39*mm,131*mm]),P('Screenshots to capture after build','h2x')]+bullets(['Homepage at desktop and mobile widths.','Collection grid with a category filter active.','Product page with a real variable product and availability state.','Bag and the configured checkout test flow; redact all customer data.'])+[P('Replace placeholder photography with licensed images. Add a working demo link only after deploying a stable staging or production site. Never publish test customer information, invented reviews, unverified sales claims or performance percentages.','bodyx'),Spacer(1,9*mm),HRFlowable(width='100%',thickness=.7,color=GOLD),Spacer(1,5*mm),P('AUREFASH','h2x'),P('Modern essentials. Quiet confidence.','smallx')]

CaseDoc(str(OUT)).build(story)
print(OUT)
