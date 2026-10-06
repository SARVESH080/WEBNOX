import collections.abc
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Exact Color Palette from Reference Image
    COLOR_BG = RGBColor(255, 255, 255)            # Pure White Background
    COLOR_NAVY = RGBColor(11, 30, 72)             # Deep Navy #0B1E48 (Titles, Header Badges)
    COLOR_BLUE_LINE = RGBColor(37, 99, 235)       # Royal Blue Accent Bar #2563EB
    COLOR_CORNER_YELLOW = RGBColor(253, 203, 85)  # Warm Gold/Yellow Top-Right Corner Accent
    COLOR_CORNER_NAVY = RGBColor(11, 30, 72)      # Deep Navy Bottom-Left Corner Accent
    COLOR_CARD_BG = RGBColor(241, 246, 254)       # Soft Ice-Blue Card Fill #F1F6FE
    COLOR_TEXT_MAIN = RGBColor(51, 65, 85)        # Slate 700 Body Text #334155
    COLOR_TEXT_BOLD = RGBColor(15, 23, 42)        # Slate 900
    COLOR_RED_HIGHLIGHT = RGBColor(225, 29, 72)   # Rose/Red for Threat highlights
    COLOR_WHITE = RGBColor(255, 255, 255)

    # Icon Circle Badge Fills & Icon Text Colors
    COLOR_BLUE_BG = RGBColor(219, 234, 254)       # Light Blue Circle
    COLOR_BLUE_ICON = RGBColor(37, 99, 235)       # Blue Icon/Text
    COLOR_GREEN_BG = RGBColor(220, 252, 231)      # Light Mint Green Circle
    COLOR_GREEN_ICON = RGBColor(22, 163, 74)      # Green Icon/Text
    COLOR_PURPLE_BG = RGBColor(243, 232, 255)     # Light Lavender Circle
    COLOR_PURPLE_ICON = RGBColor(147, 51, 234)    # Purple Icon/Text
    COLOR_YELLOW_BG = RGBColor(254, 243, 199)     # Light Amber Circle
    COLOR_YELLOW_ICON = RGBColor(217, 119, 6)     # Amber Icon/Text
    COLOR_ROSE_BG = RGBColor(255, 228, 230)       # Light Rose Circle
    COLOR_ROSE_ICON = RGBColor(225, 29, 72)       # Rose Icon/Text

    def apply_slide_template(slide, title_text):
        # 1. Base pure white background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()

        # 2. Decorative Top-Right Corner Curve (Warm Yellow)
        corner_tr = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(12.2), Inches(-0.8), Inches(2.2), Inches(2.2))
        corner_tr.fill.solid()
        corner_tr.fill.fore_color.rgb = COLOR_CORNER_YELLOW
        corner_tr.line.fill.background()

        # 3. Decorative Bottom-Left Corner Curve (Deep Navy)
        corner_bl = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(-1.0), Inches(6.3), Inches(2.4), Inches(2.4))
        corner_bl.fill.solid()
        corner_bl.fill.fore_color.rgb = COLOR_CORNER_NAVY
        corner_bl.line.fill.background()

        # 4. Slide Title (Deep Navy, Bold, Modern Sans)
        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.55), Inches(11.0), Inches(0.8))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = "Segoe UI"
        p_title.font.size = Pt(28)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_NAVY

        # 5. Short Royal Blue Accent Underline
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.82), Inches(1.38), Inches(0.9), Inches(0.06))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_BLUE_LINE
        line.line.fill.background()

    def add_icon_row(slide, x, y, icon_symbol, circle_bg, icon_col, bold_title, desc_text, width=Inches(4.5)):
        # Circle Badge
        circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y, Inches(0.58), Inches(0.58))
        circle.fill.solid()
        circle.fill.fore_color.rgb = circle_bg
        circle.line.fill.background()
        tf_c = circle.text_frame
        p_c = tf_c.paragraphs[0]
        p_c.text = icon_symbol
        p_c.font.name = "Segoe UI"
        p_c.font.size = Pt(16)
        p_c.font.bold = True
        p_c.font.color.rgb = icon_col
        p_c.alignment = PP_ALIGN.CENTER
        circle.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

        # Text Frame beside circle
        tb = slide.shapes.add_textbox(x + Inches(0.72), y - Inches(0.05), width, Inches(0.75))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = bold_title
        p.font.name = "Segoe UI"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_BOLD

        if desc_text:
            p2 = tf.add_paragraph()
            p2.text = desc_text
            p2.font.name = "Segoe UI"
            p2.font.size = Pt(11)
            p2.font.color.rgb = COLOR_TEXT_MAIN
            p2.space_before = Pt(2)

    # -------------------------------------------------------------
    # SLIDE 1: TITLE SLIDE
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    # Background
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_BG
    bg1.line.fill.background()

    # Large Top-Right Accent
    tr1 = s1.shapes.add_shape(MSO_SHAPE.OVAL, Inches(10.8), Inches(-1.5), Inches(4.2), Inches(4.2))
    tr1.fill.solid()
    tr1.fill.fore_color.rgb = COLOR_CORNER_YELLOW
    tr1.line.fill.background()

    # Large Bottom-Left Accent
    bl1 = s1.shapes.add_shape(MSO_SHAPE.OVAL, Inches(-1.5), Inches(4.8), Inches(4.5), Inches(4.5))
    bl1.fill.solid()
    bl1.fill.fore_color.rgb = COLOR_CORNER_NAVY
    bl1.line.fill.background()

    # Badge Pill
    badge1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.8), Inches(3.6), Inches(0.42))
    badge1.fill.solid()
    badge1.fill.fore_color.rgb = COLOR_CARD_BG
    badge1.line.color.rgb = COLOR_BLUE_LINE
    p_b1 = badge1.text_frame.paragraphs[0]
    p_b1.text = "CYBERSECURITY & WEB INTELLIGENCE"
    p_b1.font.name = "Segoe UI"
    p_b1.font.size = Pt(10)
    p_b1.font.bold = True
    p_b1.font.color.rgb = COLOR_BLUE_LINE
    p_b1.alignment = PP_ALIGN.CENTER
    badge1.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    # Main Title
    tb_s1 = s1.shapes.add_textbox(Inches(1.2), Inches(2.4), Inches(9.8), Inches(2.4))
    tf_s1 = tb_s1.text_frame
    tf_s1.word_wrap = True
    p_m1 = tf_s1.paragraphs[0]
    p_m1.text = "Real-Time Progressive Phishing Detection"
    p_m1.font.name = "Segoe UI"
    p_m1.font.size = Pt(40)
    p_m1.font.bold = True
    p_m1.font.color.rgb = COLOR_NAVY

    p_sub1 = tf_s1.add_paragraph()
    p_sub1.text = "Browser Extension for Detecting Known and Unseen Phishing Websites with Low Latency"
    p_sub1.font.name = "Segoe UI"
    p_sub1.font.size = Pt(18)
    p_sub1.font.color.rgb = COLOR_TEXT_MAIN
    p_sub1.space_before = Pt(12)

    # Short line
    line1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(4.9), Inches(1.4), Inches(0.07))
    line1.fill.solid()
    line1.fill.fore_color.rgb = COLOR_BLUE_LINE
    line1.line.fill.background()

    # Team & Presentation details card
    c_s1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(5.3), Inches(8.5), Inches(1.4))
    c_s1.fill.solid()
    c_s1.fill.fore_color.rgb = COLOR_CARD_BG
    c_s1.line.color.rgb = RGBColor(226, 232, 240)
    tf_cs1 = c_s1.text_frame
    tf_cs1.word_wrap = True
    p_d1 = tf_cs1.paragraphs[0]
    p_d1.text = "Fast • Real-Time • Accurate • Adaptive Web Threat Defense"
    p_d1.font.name = "Segoe UI"
    p_d1.font.size = Pt(13)
    p_d1.font.bold = True
    p_d1.font.color.rgb = COLOR_NAVY
    p_d2 = tf_cs1.add_paragraph()
    p_d2.text = "Presented by Team PhishGuard | Chrome Manifest V3 & ML Architecture"
    p_d2.font.name = "Segoe UI"
    p_d2.font.size = Pt(11)
    p_d2.font.color.rgb = COLOR_TEXT_MAIN
    p_d2.space_before = Pt(4)

    # -------------------------------------------------------------
    # SLIDE 2: PROBLEM STATEMENT (Exact Replica of Reference Image)
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    apply_slide_template(s2, "Problem Statement")

    # Left: Text Block
    tb_p = s2.shapes.add_textbox(Inches(0.8), Inches(1.85), Inches(5.8), Inches(2.6))
    tf_p = tb_p.text_frame
    tf_p.word_wrap = True
    pp = tf_p.paragraphs[0]
    pp.text = "Phishing attacks increasingly use newly created domains, deceptive URLs, and fake webpages to steal sensitive information. Traditional blacklist-based systems may miss these unknown threats, while deep analysis can cause delays and false positives. There is a need for a fast, real-time system that detects known and unseen phishing threats accurately."
    pp.font.name = "Segoe UI"
    pp.font.size = Pt(15)
    pp.font.color.rgb = COLOR_TEXT_MAIN

    # Left Bottom: Graphic Container (Simulating the Laptop / Phishing Alert Visual)
    g_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(4.6), Inches(5.2), Inches(2.2))
    g_box.fill.solid()
    g_box.fill.fore_color.rgb = RGBColor(248, 250, 252)
    g_box.line.color.rgb = RGBColor(226, 232, 240)
    tf_gb = g_box.text_frame
    tf_gb.word_wrap = True
    pgb_h = tf_gb.paragraphs[0]
    pgb_h.text = "💻 THE ATTACK VECTOR"
    pgb_h.font.name = "Segoe UI"
    pgb_h.font.size = Pt(11)
    pgb_h.font.bold = True
    pgb_h.font.color.rgb = COLOR_RED_HIGHLIGHT
    pgb_b = tf_gb.add_paragraph()
    pgb_b.text = "Fake Login Forms & Impersonated Brands\n🎣 Hook: Credentials, OTPs, and banking tokens exfiltrated\n⚠️ Threat: Zero-day URLs evade static blocklists"
    pgb_b.font.name = "Segoe UI"
    pgb_b.font.size = Pt(12)
    pgb_b.font.color.rgb = COLOR_TEXT_MAIN
    pgb_b.space_before = Pt(6)

    # Right: Need / Solution Card
    card_r = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(1.65), Inches(5.4), Inches(5.3))
    card_r.fill.solid()
    card_r.fill.fore_color.rgb = COLOR_CARD_BG
    card_r.line.fill.background()

    # Dark Pill Header
    pill_r = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.4), Inches(1.45), Inches(2.6), Inches(0.48))
    pill_r.fill.solid()
    pill_r.fill.fore_color.rgb = COLOR_NAVY
    pill_r.line.fill.background()
    p_pr = pill_r.text_frame.paragraphs[0]
    p_pr.text = "Need / Solution"
    p_pr.font.name = "Segoe UI"
    p_pr.font.size = Pt(14)
    p_pr.font.bold = True
    p_pr.font.color.rgb = COLOR_WHITE
    p_pr.alignment = PP_ALIGN.CENTER
    pill_r.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    # 4 Items inside Right Card
    items_s2 = [
        ("⚡", COLOR_BLUE_BG, COLOR_BLUE_ICON, "Detect both known and", "new (unseen) phishing threats"),
        ("🕒", COLOR_GREEN_BG, COLOR_GREEN_ICON, "Provide real-time analysis", "for faster protection"),
        ("🎯", COLOR_PURPLE_BG, COLOR_PURPLE_ICON, "Reduce false positives", "while maintaining high accuracy"),
        ("🛡️", COLOR_YELLOW_BG, COLOR_YELLOW_ICON, "Go beyond blacklists", "with AI-driven and intelligent detection")
    ]
    for i, (sym, c_bg, c_icon, bold_t, sub_t) in enumerate(items_s2):
        add_icon_row(s2, Inches(7.5), Inches(2.2 + i * 1.15), sym, c_bg, c_icon, bold_t, sub_t, width=Inches(4.2))

    # -------------------------------------------------------------
    # SLIDE 3: PROPOSED SOLUTION
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    apply_slide_template(s3, "Proposed Solution")

    # Left Column: AI-Powered Real-Time Phishing Detection Card
    card_sol = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.65), Inches(6.5), Inches(5.3))
    card_sol.fill.solid()
    card_sol.fill.fore_color.rgb = COLOR_CARD_BG
    card_sol.line.fill.background()

    pill_sol = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(1.45), Inches(3.8), Inches(0.48))
    pill_sol.fill.solid()
    pill_sol.fill.fore_color.rgb = COLOR_NAVY
    pill_sol.line.fill.background()
    psol = pill_sol.text_frame.paragraphs[0]
    psol.text = "🛡️ AI-Powered Detection"
    psol.font.name = "Segoe UI"
    psol.font.size = Pt(13)
    psol.font.bold = True
    psol.font.color.rgb = COLOR_WHITE
    psol.alignment = PP_ALIGN.CENTER
    pill_sol.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    features_s3 = [
        ("🔗", COLOR_BLUE_BG, COLOR_BLUE_ICON, "Analyze URL & webpage features instantly", "Extracts lexical and structural indicators in milliseconds"),
        ("🧠", COLOR_PURPLE_BG, COLOR_PURPLE_ICON, "ML-based detection for known and unseen threats", "Identifies zero-day attack patterns without waiting for feeds"),
        ("📋", COLOR_GREEN_BG, COLOR_GREEN_ICON, "Combine blacklists + intelligent analysis", "Leverages cached threat feeds with predictive heuristics"),
        ("⚡", COLOR_YELLOW_BG, COLOR_YELLOW_ICON, "Generate an instant risk score", "Transparent 0-100 rating with explainable alerts")
    ]
    for i, (sym, c_bg, c_icon, b_t, s_t) in enumerate(features_s3):
        add_icon_row(s3, Inches(1.1), Inches(2.2 + i * 1.15), sym, c_bg, c_icon, b_t, s_t, width=Inches(5.3))

    # Right Column: Output Triage & User Warning System
    card_out = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.6), Inches(1.65), Inches(4.9), Inches(5.3))
    card_out.fill.solid()
    card_out.fill.fore_color.rgb = COLOR_CARD_BG
    card_out.line.fill.background()

    pill_out = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.9), Inches(1.45), Inches(3.0), Inches(0.48))
    pill_out.fill.solid()
    pill_out.fill.fore_color.rgb = COLOR_NAVY
    pill_out.line.fill.background()
    pout = pill_out.text_frame.paragraphs[0]
    pout.text = "Actionable Output"
    pout.font.name = "Segoe UI"
    pout.font.size = Pt(13)
    pout.font.bold = True
    pout.font.color.rgb = COLOR_WHITE
    pout.alignment = PP_ALIGN.CENTER
    pill_out.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    # 3 Status Badges
    outputs = [
        ("🟢 SAFE", COLOR_GREEN_BG, COLOR_GREEN_ICON, "Verified Safe Website", "No significant threat indicators detected. Normal browsing allowed with zero added latency."),
        ("🟠 SUSPICIOUS", COLOR_YELLOW_BG, COLOR_YELLOW_ICON, "Caution Recommended", "Unknown domain with anomalous characteristics. Warns user to verify before entering details."),
        ("🔴 PHISHING", COLOR_ROSE_BG, COLOR_ROSE_ICON, "High-Risk Threat Blocked", "Impersonation and credential-harvesting detected. Intercepts connection immediately.")
    ]
    for i, (tag, c_bg, c_icon, b_t, s_t) in enumerate(outputs):
        box_out = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.9), Inches(2.15 + i * 1.45), Inches(4.3), Inches(1.28))
        box_out.fill.solid()
        box_out.fill.fore_color.rgb = COLOR_WHITE
        box_out.line.color.rgb = RGBColor(226, 232, 240)
        tf_bo = box_out.text_frame
        tf_bo.word_wrap = True
        
        p_btag = tf_bo.paragraphs[0]
        p_btag.text = f"{tag} — {b_t}"
        p_btag.font.name = "Segoe UI"
        p_btag.font.size = Pt(12)
        p_btag.font.bold = True
        p_btag.font.color.rgb = c_icon
        
        p_bdesc = tf_bo.add_paragraph()
        p_bdesc.text = s_t
        p_bdesc.font.name = "Segoe UI"
        p_bdesc.font.size = Pt(10)
        p_bdesc.font.color.rgb = COLOR_TEXT_MAIN
        p_bdesc.space_before = Pt(3)

    # -------------------------------------------------------------
    # SLIDE 4: TECHNICAL APPROACH
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    apply_slide_template(s4, "Technical Approach")

    # Left: Frontend & Extension Stack
    card_tech1 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.65), Inches(4.8), Inches(5.3))
    card_tech1.fill.solid()
    card_tech1.fill.fore_color.rgb = COLOR_CARD_BG
    card_tech1.line.fill.background()

    pill_t1 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(1.45), Inches(3.2), Inches(0.48))
    pill_t1.fill.solid()
    pill_t1.fill.fore_color.rgb = COLOR_NAVY
    pill_t1.line.fill.background()
    pt1 = pill_t1.text_frame.paragraphs[0]
    pt1.text = "💻 Frontend Stack"
    pt1.font.name = "Segoe UI"
    pt1.font.size = Pt(13)
    pt1.font.bold = True
    pt1.font.color.rgb = COLOR_WHITE
    pt1.alignment = PP_ALIGN.CENTER
    pill_t1.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    tech_items = [
        ("🌐", COLOR_BLUE_BG, COLOR_BLUE_ICON, "HTML5", "Structured interface & responsive web layout"),
        ("🎨", COLOR_GREEN_BG, COLOR_GREEN_ICON, "CSS3 / Tailwind CSS", "Modern cybersecurity visual styling"),
        ("⚡", COLOR_YELLOW_BG, COLOR_YELLOW_ICON, "JavaScript (ES6+)", "URL handling & real-time async DOM events"),
        ("🧩", COLOR_PURPLE_BG, COLOR_PURPLE_ICON, "Chrome Manifest V3", "Lightweight browser extension background worker"),
        ("⚛️", COLOR_BLUE_BG, COLOR_BLUE_ICON, "React.js / Next.js", "Interactive evaluator & threat risk dashboard")
    ]
    for i, (sym, c_bg, c_icon, b_t, s_t) in enumerate(tech_items):
        add_icon_row(s4, Inches(1.0), Inches(2.15 + i * 0.95), sym, c_bg, c_icon, b_t, s_t, width=Inches(3.8))

    # Right: Detection Pipeline & Analyzed Features
    card_tech2 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.9), Inches(1.65), Inches(6.6), Inches(5.3))
    card_tech2.fill.solid()
    card_tech2.fill.fore_color.rgb = COLOR_CARD_BG
    card_tech2.line.fill.background()

    pill_t2 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.2), Inches(1.45), Inches(3.6), Inches(0.48))
    pill_t2.fill.solid()
    pill_t2.fill.fore_color.rgb = COLOR_NAVY
    pill_t2.line.fill.background()
    pt2 = pill_t2.text_frame.paragraphs[0]
    pt2.text = "⚙️ Detection Pipeline"
    pt2.font.name = "Segoe UI"
    pt2.font.size = Pt(13)
    pt2.font.bold = True
    pt2.font.color.rgb = COLOR_WHITE
    pt2.alignment = PP_ALIGN.CENTER
    pill_t2.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    # Pipeline Flow Banner Box
    flow_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.2), Inches(2.1), Inches(6.0), Inches(0.95))
    flow_box.fill.solid()
    flow_box.fill.fore_color.rgb = COLOR_WHITE
    flow_box.line.color.rgb = COLOR_BLUE_LINE
    tf_fb = flow_box.text_frame
    tf_fb.word_wrap = True
    p_fbt = tf_fb.paragraphs[0]
    p_fbt.text = "URL  ➔  Feature Extraction  ➔  Blacklist Check  ➔  ML Model  ➔  Risk Score  ➔  Alert"
    p_fbt.font.name = "Segoe UI"
    p_fbt.font.size = Pt(11)
    p_fbt.font.bold = True
    p_fbt.font.color.rgb = COLOR_NAVY
    p_fbt.alignment = PP_ALIGN.CENTER
    flow_box.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    # Features Analyzed
    tb_feat = s4.shapes.add_textbox(Inches(6.2), Inches(3.2), Inches(6.0), Inches(0.4))
    p_fth = tb_feat.text_frame.paragraphs[0]
    p_fth.text = "🔍 KEY FEATURES ANALYZED"
    p_fth.font.name = "Segoe UI"
    p_fth.font.size = Pt(12)
    p_fth.font.bold = True
    p_fth.font.color.rgb = COLOR_BLUE_LINE

    features_list = [
        ("📏", COLOR_BLUE_BG, COLOR_BLUE_ICON, "URL Structure & Length", "Entropy, dot counts, special characters (@, -, //), and direct IP URLs"),
        ("🏷️", COLOR_GREEN_BG, COLOR_GREEN_ICON, "Domain Characteristics", "Subdomain depth, TLD reputation (.xyz, .top), and age markers"),
        ("🔒", COLOR_YELLOW_BG, COLOR_YELLOW_ICON, "HTTPS / SSL Information", "Certificate authority validity, self-signed alerts, and protocol security"),
        ("🔀", COLOR_PURPLE_BG, COLOR_PURPLE_ICON, "Redirects & Form Patterns", "Hidden multi-hop redirects and credential input targets pointing off-domain")
    ]
    for i, (sym, c_bg, c_icon, b_t, s_t) in enumerate(features_list):
        add_icon_row(s4, Inches(6.2), Inches(3.65 + i * 0.82), sym, c_bg, c_icon, b_t, s_t, width=Inches(5.3))

    # -------------------------------------------------------------
    # SLIDE 5: FEASIBILITY & IMPLEMENTATION
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    apply_slide_template(s5, "Feasibility & Implementation")

    # Left: Technically Feasible
    card_f1 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.65), Inches(5.4), Inches(5.3))
    card_f1.fill.solid()
    card_f1.fill.fore_color.rgb = COLOR_CARD_BG
    card_f1.line.fill.background()

    pill_f1 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(1.45), Inches(3.4), Inches(0.48))
    pill_f1.fill.solid()
    pill_f1.fill.fore_color.rgb = COLOR_NAVY
    pill_f1.line.fill.background()
    pf1 = pill_f1.text_frame.paragraphs[0]
    pf1.text = "✅ Technically Feasible"
    pf1.font.name = "Segoe UI"
    pf1.font.size = Pt(13)
    pf1.font.bold = True
    pf1.font.color.rgb = COLOR_WHITE
    pf1.alignment = PP_ALIGN.CENTER
    pill_f1.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    feasibility_pts = [
        ("🧩", COLOR_BLUE_BG, COLOR_BLUE_ICON, "Lightweight Browser Architecture", "Runs via Manifest V3 without impacting browser memory or speed"),
        ("🔓", COLOR_GREEN_BG, COLOR_GREEN_ICON, "Open-Source Technologies", "Built with proven web standards, Scikit-learn/XGBoost, and FastAPI"),
        ("⚡", COLOR_YELLOW_BG, COLOR_YELLOW_ICON, "Zero-Friction User Experience", "Operates automatically in the background with minimal user interaction"),
        ("🎯", COLOR_PURPLE_BG, COLOR_PURPLE_ICON, "Rapid MVP Delivery", "Core MVP achievable using HTML + CSS + JavaScript + Python")
    ]
    for i, (sym, c_bg, c_icon, b_t, s_t) in enumerate(feasibility_pts):
        add_icon_row(s5, Inches(1.0), Inches(2.2 + i * 1.15), sym, c_bg, c_icon, b_t, s_t, width=Inches(4.4))

    # Right: Implementation Phases & MVP
    card_f2 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.5), Inches(1.65), Inches(6.0), Inches(5.3))
    card_f2.fill.solid()
    card_f2.fill.fore_color.rgb = COLOR_CARD_BG
    card_f2.line.fill.background()

    pill_f2 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.45), Inches(3.2), Inches(0.48))
    pill_f2.fill.solid()
    pill_f2.fill.fore_color.rgb = COLOR_NAVY
    pill_f2.line.fill.background()
    pf2 = pill_f2.text_frame.paragraphs[0]
    pf2.text = "🚀 Implementation"
    pf2.font.name = "Segoe UI"
    pf2.font.size = Pt(13)
    pf2.font.bold = True
    pf2.font.color.rgb = COLOR_WHITE
    pf2.alignment = PP_ALIGN.CENTER
    pill_f2.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    phases = [
        ("1", COLOR_BLUE_BG, COLOR_BLUE_ICON, "Phase 1: Dataset & Feature Engineering", "PhishTank, Tranco 1M, and URL structural lexical extraction"),
        ("2", COLOR_GREEN_BG, COLOR_GREEN_ICON, "Phase 2: ML Model Development", "Training zero-day classifiers with low false-positive constraints"),
        ("3", COLOR_YELLOW_BG, COLOR_YELLOW_ICON, "Phase 3: Browser Extension Integration", "Manifest V3 background worker, content script & warning UI"),
        ("4", COLOR_PURPLE_BG, COLOR_PURPLE_ICON, "Phase 4: Real-Time Testing & Optimization", "Sub-50ms latency benchmarking, false-positive tuning & audit")
    ]
    for i, (sym, c_bg, c_icon, b_t, s_t) in enumerate(phases):
        add_icon_row(s5, Inches(6.8), Inches(2.15 + i * 0.95), sym, c_bg, c_icon, b_t, s_t, width=Inches(4.9))

    # MVP Callout Box
    mvp_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(5.9), Inches(5.4), Inches(0.85))
    mvp_box.fill.solid()
    mvp_box.fill.fore_color.rgb = COLOR_WHITE
    mvp_box.line.color.rgb = COLOR_BLUE_LINE
    tf_mvp = mvp_box.text_frame
    tf_mvp.word_wrap = True
    pmvp_t = tf_mvp.paragraphs[0]
    pmvp_t.text = "🎯 OUR MVP SPECIFICATION"
    pmvp_t.font.name = "Segoe UI"
    pmvp_t.font.size = Pt(10)
    pmvp_t.font.bold = True
    pmvp_t.font.color.rgb = COLOR_BLUE_LINE
    pmvp_b = tf_mvp.add_paragraph()
    pmvp_b.text = "Chrome Extension + Detection API + Live Risk Dashboard"
    pmvp_b.font.name = "Segoe UI"
    pmvp_b.font.size = Pt(13)
    pmvp_b.font.bold = True
    pmvp_b.font.color.rgb = COLOR_NAVY
    pmvp_b.space_before = Pt(2)

    # -------------------------------------------------------------
    # SLIDE 6: IMPACT & BENEFITS
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    apply_slide_template(s6, "Impact & Benefits")

    col_data_s6 = [
        ("🛡️ User Protection", COLOR_BLUE_BG, COLOR_BLUE_ICON, [
            ("Detects Unknown Threats", "Identifies newly registered phishing domains before blacklists index them."),
            ("Real-Time Warnings", "Warns users instantly before passwords or OTPs are entered."),
            ("Protects Sensitive Data", "Secures banking credentials, personal information, and corporate accounts.")
        ]),
        ("⚡ Performance", COLOR_GREEN_BG, COLOR_GREEN_ICON, [
            ("Low-Latency Analysis", "Progressive checks prevent annoying browsing delays (<50ms)."),
            ("Reduced False Alerts", "Intelligent allowlists protect everyday work tools and legitimate SSO."),
            ("Frictionless UI", "Clean, non-intrusive alerts that clearly explain the risk level.")
        ]),
        ("🌍 Wider Impact", COLOR_PURPLE_BG, COLOR_PURPLE_ICON, [
            ("Broad Accessibility", "Protects students, regular internet users, and large enterprise workforces."),
            ("Safer Digital Economy", "Fosters trust in online banking, e-commerce, and public digital services."),
            ("Continuously Adaptive", "Improves threat models over time with incoming attack intelligence.")
        ])
    ]

    card_w = Inches(3.7)
    card_gap = Inches(0.3)
    for i, (title, c_bg, c_icon, items) in enumerate(col_data_s6):
        x = Inches(0.8) + i * (card_w + card_gap)
        c_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.65), card_w, Inches(5.3))
        c_box.fill.solid()
        c_box.fill.fore_color.rgb = COLOR_CARD_BG
        c_box.line.fill.background()

        # Pill Header
        pill = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.2), Inches(1.45), Inches(3.3), Inches(0.48))
        pill.fill.solid()
        pill.fill.fore_color.rgb = COLOR_NAVY
        pill.line.fill.background()
        ppl = pill.text_frame.paragraphs[0]
        ppl.text = title
        ppl.font.name = "Segoe UI"
        ppl.font.size = Pt(13)
        ppl.font.bold = True
        ppl.font.color.rgb = COLOR_WHITE
        ppl.alignment = PP_ALIGN.CENTER
        pill.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

        for j, (bold_txt, desc_txt) in enumerate(items):
            box_item = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.25), Inches(2.15 + j * 1.55), Inches(3.2), Inches(1.35))
            box_item.fill.solid()
            box_item.fill.fore_color.rgb = COLOR_WHITE
            box_item.line.color.rgb = RGBColor(226, 232, 240)
            tf_bi = box_item.text_frame
            tf_bi.word_wrap = True
            
            p1 = tf_bi.paragraphs[0]
            p1.text = f"✔ {bold_txt}"
            p1.font.name = "Segoe UI"
            p1.font.size = Pt(12)
            p1.font.bold = True
            p1.font.color.rgb = c_icon
            
            p2 = tf_bi.add_paragraph()
            p2.text = desc_txt
            p2.font.name = "Segoe UI"
            p2.font.size = Pt(10)
            p2.font.color.rgb = COLOR_TEXT_MAIN
            p2.space_before = Pt(4)

    # -------------------------------------------------------------
    # SLIDE 7: WHAT'S NEW? (OUR INNOVATION)
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    apply_slide_template(s7, "What's New? Our Innovation")

    # Innovation Points Grid (2 Columns x 3 Rows)
    innovations = [
        ("🔄", COLOR_BLUE_BG, COLOR_BLUE_ICON, "Beyond Blacklists", "Detects underlying behavioral & structural patterns in unseen domains."),
        ("🧠", COLOR_PURPLE_BG, COLOR_PURPLE_ICON, "Hybrid Intelligence", "Combines threat intelligence feeds + ML classification + local rules."),
        ("⚡", COLOR_YELLOW_BG, COLOR_YELLOW_ICON, "Real-Time Detection", "Sub-50ms lightweight execution directly while users browse."),
        ("🔍", COLOR_GREEN_BG, COLOR_GREEN_ICON, "Explainable Alerts", "Shows transparent indicators (e.g., brand mismatch, fake login form)."),
        ("🎯", COLOR_BLUE_BG, COLOR_BLUE_ICON, "Risk-Based Classification", "Calibrated 3-tier output (Safe / Suspicious / High-Risk Phishing)."),
        ("🧩", COLOR_ROSE_BG, COLOR_ROSE_ICON, "Lightweight Extension", "In-browser protection with zero intrusive proxies or privacy leaks.")
    ]

    for i, (sym, c_bg, c_icon, b_t, s_t) in enumerate(innovations):
        col = i % 2
        row = i // 2
        x = Inches(0.8) + col * Inches(6.0)
        y = Inches(1.65) + row * Inches(1.35)

        c_inn = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.7), Inches(1.18))
        c_inn.fill.solid()
        c_inn.fill.fore_color.rgb = COLOR_CARD_BG
        c_inn.line.color.rgb = RGBColor(226, 232, 240)

        add_icon_row(s7, x + Inches(0.2), y + Inches(0.2), sym, c_bg, c_icon, b_t, s_t, width=Inches(4.5))

    # Bottom Key Idea Banner
    key_box = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.85), Inches(11.7), Inches(1.15))
    key_box.fill.solid()
    key_box.fill.fore_color.rgb = COLOR_NAVY
    key_box.line.fill.background()
    tf_kb = key_box.text_frame
    tf_kb.word_wrap = True

    p_kbl = tf_kb.paragraphs[0]
    p_kbl.text = "CORE ARCHITECTURAL PHILOSOPHY"
    p_kbl.font.name = "Segoe UI"
    p_kbl.font.size = Pt(10)
    p_kbl.font.bold = True
    p_kbl.font.color.rgb = COLOR_CORNER_YELLOW
    p_kbl.alignment = PP_ALIGN.CENTER

    p_kb = tf_kb.add_paragraph()
    p_kb.text = "“Detect the pattern, not just the website.”"
    p_kb.font.name = "Segoe UI"
    p_kb.font.size = Pt(22)
    p_kb.font.bold = True
    p_kb.font.color.rgb = COLOR_WHITE
    p_kb.alignment = PP_ALIGN.CENTER
    p_kb.space_before = Pt(4)

    # -------------------------------------------------------------
    # SLIDE 8: PROTOTYPE • FUTURE ROADMAP • REFERENCES
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    apply_slide_template(s8, "Prototype • Future Roadmap • References")

    # 1. Left: Prototype Flow (4.0 in)
    cp = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.65), Inches(3.8), Inches(5.3))
    cp.fill.solid()
    cp.fill.fore_color.rgb = COLOR_CARD_BG
    cp.line.fill.background()

    pill_p = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.45), Inches(2.6), Inches(0.48))
    pill_p.fill.solid()
    pill_p.fill.fore_color.rgb = COLOR_NAVY
    pill_p.line.fill.background()
    pp_t = pill_p.text_frame.paragraphs[0]
    pp_t.text = "🧪 Current Prototype"
    pp_t.font.name = "Segoe UI"
    pp_t.font.size = Pt(12)
    pp_t.font.bold = True
    pp_t.font.color.rgb = COLOR_WHITE
    pp_t.alignment = PP_ALIGN.CENTER
    pill_p.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    proto_steps = [
        ("1. Chrome Extension", "Intercepts active tab URL via Manifest V3"),
        ("2. Analyze Features", "Extracts lexical, structural & brand signals"),
        ("3. Calculate Risk", "Heuristic & ML engine produces 0-100 score"),
        ("4. Display Warning", "Instant Safe / Caution / Red Block overlay")
    ]
    for i, (head, sub) in enumerate(proto_steps):
        b_p = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(2.15 + i * 1.15), Inches(3.4), Inches(0.95))
        b_p.fill.solid()
        b_p.fill.fore_color.rgb = COLOR_WHITE
        b_p.line.color.rgb = RGBColor(226, 232, 240)
        tf_bp = b_p.text_frame
        tf_bp.word_wrap = True
        p1 = tf_bp.paragraphs[0]
        p1.text = head
        p1.font.name = "Segoe UI"
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_BLUE_LINE
        p2 = tf_bp.add_paragraph()
        p2.text = sub
        p2.font.name = "Segoe UI"
        p2.font.size = Pt(10)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_before = Pt(2)

    # 2. Middle: Future Roadmap (4.5 in)
    cr = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.8), Inches(1.65), Inches(4.5), Inches(5.3))
    cr.fill.solid()
    cr.fill.fore_color.rgb = COLOR_CARD_BG
    cr.line.fill.background()

    pill_r = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.0), Inches(1.45), Inches(2.8), Inches(0.48))
    pill_r.fill.solid()
    pill_r.fill.fore_color.rgb = COLOR_NAVY
    pill_r.line.fill.background()
    pr_t = pill_r.text_frame.paragraphs[0]
    pr_t.text = "🚀 Future Roadmap"
    pr_t.font.name = "Segoe UI"
    pr_t.font.size = Pt(12)
    pr_t.font.bold = True
    pr_t.font.color.rgb = COLOR_WHITE
    pr_t.alignment = PP_ALIGN.CENTER
    pill_r.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    roadmap_items = [
        ("📱", COLOR_BLUE_BG, COLOR_BLUE_ICON, "Mobile Browser Protection", "Extension support for mobile Chrome & Safari"),
        ("🤖", COLOR_PURPLE_BG, COLOR_PURPLE_ICON, "Advanced Deep-Learning", "Transformer-based sequence character models"),
        ("🌐", COLOR_YELLOW_BG, COLOR_YELLOW_ICON, "Multilingual Phishing", "Detection tailored for regional scripts & languages"),
        ("🔄", COLOR_GREEN_BG, COLOR_GREEN_ICON, "Continuous Intelligence", "Automated threat intelligence telemetry updates"),
        ("🔐", COLOR_ROSE_BG, COLOR_ROSE_ICON, "Email & SMS Defense", "Cross-vector detection for Smishing & Quishing")
    ]
    for i, (sym, c_bg, c_icon, b_t, s_t) in enumerate(roadmap_items):
        add_icon_row(s8, Inches(5.0), Inches(2.15 + i * 0.95), sym, c_bg, c_icon, b_t, s_t, width=Inches(3.7))

    # 3. Right: References (3.0 in)
    cref = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.5), Inches(1.65), Inches(3.0), Inches(5.3))
    cref.fill.solid()
    cref.fill.fore_color.rgb = COLOR_CARD_BG
    cref.line.fill.background()

    pill_ref = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.7), Inches(1.45), Inches(2.2), Inches(0.48))
    pill_ref.fill.solid()
    pill_ref.fill.fore_color.rgb = COLOR_NAVY
    pill_ref.line.fill.background()
    prf_t = pill_ref.text_frame.paragraphs[0]
    prf_t.text = "📚 References"
    prf_t.font.name = "Segoe UI"
    prf_t.font.size = Pt(12)
    prf_t.font.bold = True
    prf_t.font.color.rgb = COLOR_WHITE
    prf_t.alignment = PP_ALIGN.CENTER
    pill_ref.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    refs = [
        ("Google Safe Browsing", "Industry standard hash-prefix reputation protocols & benchmark"),
        ("PhishTank Feed", "Community-verified repository of active phishing data"),
        ("UCI ML Repository", "Phishing Websites dataset for lexical feature engineering"),
        ("Tranco Top 1M", "Research-oriented top authority domain allowlist")
    ]
    for i, (ref_t, ref_d) in enumerate(refs):
        box_ref = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.7), Inches(2.15 + i * 1.15), Inches(2.6), Inches(0.95))
        box_ref.fill.solid()
        box_ref.fill.fore_color.rgb = COLOR_WHITE
        box_ref.line.color.rgb = RGBColor(226, 232, 240)
        tf_rf = box_ref.text_frame
        tf_rf.word_wrap = True
        
        p1 = tf_rf.paragraphs[0]
        p1.text = f"• {ref_t}"
        p1.font.name = "Segoe UI"
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_NAVY
        
        p2 = tf_rf.add_paragraph()
        p2.text = ref_d
        p2.font.name = "Segoe UI"
        p2.font.size = Pt(9)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_before = Pt(2)

    # Save presentation
    output_path = r"e:\INSTA AUTOMATION\PhishGuard_Matched_Style_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation successfully saved to: {output_path}")

if __name__ == "__main__":
    build_presentation()
