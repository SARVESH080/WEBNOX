import collections.abc
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_sih_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # SIH Cybersecurity Color Theme
    BG_COLOR = RGBColor(11, 20, 38)        # Deep Navy / Dark Cybersecurity #0B1426
    CARD_BG = RGBColor(20, 34, 61)         # Navy Card #14223D
    CARD_BORDER = RGBColor(40, 65, 110)    # Subdued Slate-Navy Border
    ACCENT_CYAN = RGBColor(0, 212, 255)    # Vibrant SIH Tech Cyan #00D4FF
    TEXT_WHITE = RGBColor(248, 250, 252)   # Pure White Text
    TEXT_MUTED = RGBColor(156, 175, 204)   # Soft Gray-Blue Text
    GREEN_SAFE = RGBColor(34, 197, 94)     # Emerald Green
    YELLOW_WARN = RGBColor(245, 158, 11)   # Amber Warning
    RED_ALERT = RGBColor(239, 68, 68)      # Crimson Red
    ROSE = RGBColor(251, 113, 133)         # Soft Rose
    ACCENT_BLUE = RGBColor(37, 99, 235)    # Royal Blue

    def set_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category="SMART INDIA HACKATHON"):
        # Category Badge
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        p_cat = cat_box.text_frame.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_CYAN

        # Title Text
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.75))
        p_t = t_box.text_frame.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(23)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE

    # -------------------------------------------------------------
    # SLIDE 1: TITLE SLIDE
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1)

    # Hackathon Tag Badge
    badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.3), Inches(4.5), Inches(0.42))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(16, 42, 77)
    badge.line.color.rgb = ACCENT_CYAN
    p_b = badge.text_frame.paragraphs[0]
    p_b.text = "SMART INDIA HACKATHON (SIH) | SOFTWARE"
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_CYAN
    p_b.alignment = PP_ALIGN.CENTER

    # Project Title & Subtitle Box
    tb_title = s1.shapes.add_textbox(Inches(0.8), Inches(1.9), Inches(11.7), Inches(2.6))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    p1 = tf_title.paragraphs[0]
    p1.text = "Real-Time Progressive Phishing Detection\nBrowser Extension"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE

    p2 = tf_title.add_paragraph()
    p2.text = "Detecting known and previously unseen phishing websites with low-latency analysis"
    p2.font.size = Pt(18)
    p2.font.color.rgb = ACCENT_CYAN
    p2.space_before = Pt(12)

    # Details Cards (Team, Members, Institution)
    col_w = Inches(3.7)
    gap = Inches(0.3)
    details = [
        ("TEAM DETAILS", "Team Name: [Your Team Name]\nTrack: Cybersecurity & AI\nProblem Category: Web Security"),
        ("TEAM MEMBERS", "• [Leader Name] (Lead / Ext Developer)\n• [Member 2] (ML / Backend)\n• [Member 3] (Frontend / Security)\n• [Member 4] (Research / QA)"),
        ("INSTITUTION", "College: [Your College / University Name]\nDepartment of Computer Science & Engg.\nAcademic Year: 2024-2025")
    ]

    for i, (head, content) in enumerate(details):
        x = Inches(0.8) + i * (col_w + gap)
        card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(4.8), col_w, Inches(2.1))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER
        tf = card.text_frame
        tf.word_wrap = True
        
        ph = tf.paragraphs[0]
        ph.text = head
        ph.font.size = Pt(12)
        ph.font.bold = True
        ph.font.color.rgb = ACCENT_CYAN
        
        pc = tf.add_paragraph()
        pc.text = content
        pc.font.size = Pt(11)
        pc.font.color.rgb = TEXT_MUTED
        pc.space_before = Pt(6)

    # -------------------------------------------------------------
    # SLIDE 2: WHAT IS THE PROBLEM?
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2)
    add_header(s2, "What is Phishing? Understanding the Threat", "01 / THREAT CONTEXT")

    # Flow Banner: User -> Fake Website -> Sensitive Information Stolen
    flow_steps = [
        ("1. Unsuspecting User", "Visits link via email, SMS, or search result", CARD_BORDER),
        ("2. Fake Website", "Imitates bank, e-commerce, or portal with precision", RED_ALERT),
        ("3. Data Exfiltration", "User credentials and financial tokens get stolen", YELLOW_WARN)
    ]
    for i, (title, sub, col) in enumerate(flow_steps):
        box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i * 4.0), Inches(1.6), Inches(3.7), Inches(1.3))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = col
        tf = box.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = col
        p_s = tf.add_paragraph()
        p_s.text = sub
        p_s.font.size = Pt(11)
        p_s.font.color.rgb = TEXT_WHITE
        p_s.space_before = Pt(4)

    # Lower Section: Left (Common Targets) | Right (Stolen Information)
    card_l = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.2), Inches(5.7), Inches(3.7))
    card_l.fill.solid()
    card_l.fill.fore_color.rgb = CARD_BG
    card_l.line.color.rgb = CARD_BORDER
    tf_l = card_l.text_frame
    tf_l.word_wrap = True
    pl_h = tf_l.paragraphs[0]
    pl_h.text = "Commonly Impersonated Targets"
    pl_h.font.size = Pt(16)
    pl_h.font.bold = True
    pl_h.font.color.rgb = ACCENT_CYAN

    targets = [
        "• Net Banking & Digital Payment Portals (UPI, RBI, major banks)",
        "• E-Commerce Platforms (fake sales, cloned checkout forms)",
        "• Government Citizen Services (tax portals, utility payment sites)",
        "• Educational Institutions & Examination Gateways",
        "• Corporate Single-Sign-On (SSO) & Email Services"
    ]
    for t in targets:
        p = tf_l.add_paragraph()
        p.text = t
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_WHITE
        p.space_before = Pt(8)

    card_r = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(3.2), Inches(5.7), Inches(3.7))
    card_r.fill.solid()
    card_r.fill.fore_color.rgb = CARD_BG
    card_r.line.color.rgb = CARD_BORDER
    tf_r = card_r.text_frame
    tf_r.word_wrap = True
    pr_h = tf_r.paragraphs[0]
    pr_h.text = "Sensitive Information Stolen"
    pr_h.font.size = Pt(16)
    pr_h.font.bold = True
    pr_h.font.color.rgb = RED_ALERT

    stolen = [
        "🔑 Account Passwords & Master Keys",
        "📱 One-Time Passwords (OTPs) intercepted in real time",
        "💳 Debit/Credit Card Numbers, CVVs & Expiry Dates",
        "🆔 Personally Identifiable Information (Aadhaar, PAN, SSN)",
        "💼 Corporate Credentials for secondary network attacks"
    ]
    for s in stolen:
        p = tf_r.add_paragraph()
        p.text = s
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_WHITE
        p.space_before = Pt(8)

    # -------------------------------------------------------------
    # SLIDE 3: PROBLEM STATEMENT
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3)
    add_header(s3, "Problem Statement: The Two Core Bottlenecks", "02 / THE CHALLENGE")

    # Main Problem Quote Box
    qbox = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(1.5))
    qbox.fill.solid()
    qbox.fill.fore_color.rgb = RGBColor(16, 42, 77)
    qbox.line.color.rgb = ACCENT_CYAN
    tf_q = qbox.text_frame
    tf_q.word_wrap = True
    pq1 = tf_q.paragraphs[0]
    pq1.text = "CORE REALITY IN PHISHING DEFENSE:"
    pq1.font.size = Pt(11)
    pq1.font.bold = True
    pq1.font.color.rgb = ACCENT_CYAN
    pq2 = tf_q.add_paragraph()
    pq2.text = "“Existing phishing protection can identify many known malicious websites, but attackers continuously create new phishing domains that may not yet appear in threat databases. Deep analysis of every website can also introduce unnecessary latency.”"
    pq2.font.size = Pt(14)
    pq2.font.color.rgb = TEXT_WHITE
    pq2.space_before = Pt(6)

    # Two Main Challenge Cards
    ch1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.4), Inches(5.7), Inches(3.5))
    ch1.fill.solid()
    ch1.fill.fore_color.rgb = CARD_BG
    ch1.line.color.rgb = RED_ALERT
    tf_c1 = ch1.text_frame
    tf_c1.word_wrap = True
    pc1_h = tf_c1.paragraphs[0]
    pc1_h.text = "Challenge 1: Unseen / Zero-Day Domains"
    pc1_h.font.size = Pt(16)
    pc1_h.font.bold = True
    pc1_h.font.color.rgb = RED_ALERT
    c1_pts = [
        "• Attackers spin up disposable phishing websites in minutes.",
        "• Threat databases require hours or days to discover, report, and blacklist new URLs.",
        "• The most critical credential theft occurs during this unindexed gap."
    ]
    for pt in c1_pts:
        p = tf_c1.add_paragraph()
        p.text = pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MUTED
        p.space_before = Pt(10)

    ch2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(3.4), Inches(5.7), Inches(3.5))
    ch2.fill.solid()
    ch2.fill.fore_color.rgb = CARD_BG
    ch2.line.color.rgb = YELLOW_WARN
    tf_c2 = ch2.text_frame
    tf_c2.word_wrap = True
    pc2_h = tf_c2.paragraphs[0]
    pc2_h.text = "Challenge 2: Low-Latency Early Warning"
    pc2_h.font.size = Pt(16)
    pc2_h.font.bold = True
    pc2_h.font.color.rgb = YELLOW_WARN
    c2_pts = [
        "• Deep cloud sandboxing or complete page re-crawling adds 2–4 seconds of delay per click.",
        "• Browsers cannot delay every legitimate website visit without destroying user experience.",
        "• Detection must warn users before credentials are typed into forms."
    ]
    for pt in c2_pts:
        p = tf_c2.add_paragraph()
        p.text = pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MUTED
        p.space_before = Pt(10)

    # -------------------------------------------------------------
    # SLIDE 4: EXISTING SOLUTIONS & LIMITATIONS
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4)
    add_header(s4, "Existing Solutions and Their Practical Limitation", "03 / CURRENT APPROACHES")

    # Current Approaches List
    approaches = [
        ("Browser Phishing Protection", "Built-in browser defenses (Google Safe Browsing, SmartScreen)."),
        ("Threat Intelligence Databases", "Global repositories tracking known malicious indicators (PhishTank, OpenPhish)."),
        ("URL Reputation Systems", "Domain scoring based on historical DNS, WHOIS, and web crawler reports."),
        ("Static Blacklists", "Pre-compiled lists of blocked domains updated periodically."),
        ("ML-Based Detection Models", "Algorithms classifying malicious URLs based on training datasets.")
    ]

    card_app = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.3))
    card_app.fill.solid()
    card_app.fill.fore_color.rgb = CARD_BG
    card_app.line.color.rgb = CARD_BORDER
    tf_app = card_app.text_frame
    tf_app.word_wrap = True
    pa_h = tf_app.paragraphs[0]
    pa_h.text = "Current Industry Approaches"
    pa_h.font.size = Pt(16)
    pa_h.font.bold = True
    pa_h.font.color.rgb = ACCENT_CYAN

    for title, desc in approaches:
        p = tf_app.add_paragraph()
        p.text = f"• {title}: {desc}"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_before = Pt(10)

    # Right side: Simple Traditional Flow Diagram + Limitation
    flow_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(1.6), Inches(5.4), Inches(2.3))
    flow_box.fill.solid()
    flow_box.fill.fore_color.rgb = RGBColor(16, 32, 58)
    flow_box.line.color.rgb = CARD_BORDER
    tf_fb = flow_box.text_frame
    tf_fb.word_wrap = True
    pf_h = tf_fb.paragraphs[0]
    pf_h.text = "TRADITIONAL DETECTION WORKFLOW"
    pf_h.font.size = Pt(11)
    pf_h.font.bold = True
    pf_h.font.color.rgb = ACCENT_CYAN

    pf_d = tf_fb.add_paragraph()
    pf_d.text = "Website URL  ➔  Reputation Database  ➔  Known Threat?  ➔  Warning / Block"
    pf_d.font.size = Pt(13)
    pf_d.font.bold = True
    pf_d.font.color.rgb = TEXT_WHITE
    pf_d.space_before = Pt(12)

    # The Core Limitation Box
    lim_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(4.2), Inches(5.4), Inches(2.7))
    lim_box.fill.solid()
    lim_box.fill.fore_color.rgb = CARD_BG
    lim_box.line.color.rgb = RED_ALERT
    tf_lim = lim_box.text_frame
    tf_lim.word_wrap = True
    plm_h = tf_lim.paragraphs[0]
    plm_h.text = "THE FUNDAMENTAL LIMITATION"
    plm_h.font.size = Pt(12)
    plm_h.font.bold = True
    plm_h.font.color.rgb = RED_ALERT

    plm_q = tf_lim.add_paragraph()
    plm_q.text = "“Unknown or newly created phishing websites may not yet have reputation information.”"
    plm_q.font.size = Pt(14)
    plm_q.font.bold = True
    plm_q.font.color.rgb = TEXT_WHITE
    plm_q.space_before = Pt(8)

    plm_desc = tf_lim.add_paragraph()
    plm_desc.text = "Existing browsers are effective against established threats, but need real-time multi-stage intelligence to handle the initial hours of new campaigns without slowing down safe websites."
    plm_desc.font.size = Pt(11)
    plm_desc.font.color.rgb = TEXT_MUTED
    plm_desc.space_before = Pt(8)

    # -------------------------------------------------------------
    # SLIDE 5: OUR PROPOSED SOLUTION
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5)
    add_header(s5, "Proposed Solution: Real-Time Progressive Phishing Detection", "04 / OUR SOLUTION")

    # High-level Concept Banner
    sol_ban = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(1.2))
    sol_ban.fill.solid()
    sol_ban.fill.fore_color.rgb = RGBColor(16, 42, 77)
    sol_ban.line.color.rgb = ACCENT_CYAN
    tf_sb = sol_ban.text_frame
    tf_sb.word_wrap = True
    psb_1 = tf_sb.paragraphs[0]
    psb_1.text = "PROGRESSIVE MULTI-STAGE ANALYSIS CONCEPT"
    psb_1.font.size = Pt(11)
    psb_1.font.bold = True
    psb_1.font.color.rgb = ACCENT_CYAN
    psb_2 = tf_sb.add_paragraph()
    psb_2.text = "The browser extension analyzes URLs in multiple stages. Fast and lightweight checks happen first, while deeper analysis is performed only when a URL is suspicious or unknown."
    psb_2.font.size = Pt(13)
    psb_2.font.color.rgb = TEXT_WHITE
    psb_2.space_before = Pt(4)

    # Pipeline Flow Visual: 6 Steps
    pipeline_steps = [
        ("1. URL Request", "Browser intercepts navigation event", CARD_BORDER),
        ("2. Local URL Check", "Rapid on-device heuristic inspection", ACCENT_CYAN),
        ("3. Threat Intel", "Reputation & known-threat check", ACCENT_BLUE),
        ("4. Domain Intel", "Age, DNS, and hosting validation", YELLOW_WARN),
        ("5. ML Analysis", "Webpage & form feature evaluation", RED_ALERT),
        ("6. Risk Score", "SAFE / SUSPICIOUS / HIGH RISK", GREEN_SAFE)
    ]

    step_w = Inches(1.75)
    step_gap = Inches(0.24)
    for i, (title, sub, col) in enumerate(pipeline_steps):
        x = Inches(0.8) + i * (step_w + step_gap)
        box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(3.1), step_w, Inches(3.8))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = col
        tf = box.text_frame
        tf.word_wrap = True
        
        p_num = tf.paragraphs[0]
        p_num.text = f"STEP 0{i+1}"
        p_num.font.size = Pt(10)
        p_num.font.bold = True
        p_num.font.color.rgb = col
        
        p_h = tf.add_paragraph()
        p_h.text = title
        p_h.font.size = Pt(14)
        p_h.font.bold = True
        p_h.font.color.rgb = TEXT_WHITE
        p_h.space_before = Pt(6)
        
        p_s = tf.add_paragraph()
        p_s.text = sub
        p_s.font.size = Pt(11)
        p_s.font.color.rgb = TEXT_MUTED
        p_s.space_before = Pt(10)

    # -------------------------------------------------------------
    # SLIDE 6: HOW IT WORKS (THE 4 LAYERS)
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6)
    add_header(s6, "How It Works: The 4-Layer Inspection Pipeline", "05 / TECHNICAL BREAKDOWN")

    layers = [
        ("1. Local URL Analysis", [
            "• URL length & structure",
            "• Suspicious keywords (login, verify)",
            "• Unusual / special characters",
            "• Excessive subdomains",
            "• Direct IP-based URLs",
            "• Look-alike / homoglyph domains"
        ], ACCENT_CYAN),
        ("2. Threat Intelligence", [
            "• Known phishing URL feeds",
            "• Malicious domain registries",
            "• Compromised host records",
            "• Previous campaign signatures",
            "• Fast cached reputation lookups",
            "• Community threat reports"
        ], ACCENT_BLUE),
        ("3. Domain Intelligence", [
            "• Newly registered domain age",
            "• DNS record consistency",
            "• SSL / TLS certificate details",
            "• ASN & hosting infrastructure",
            "• Geographic hosting anomalies",
            "• Registrar history checks"
        ], YELLOW_WARN),
        ("4. ML / Webpage Analysis", [
            "• Suspicious login form inputs",
            "• Foreign form submission actions",
            "• Brand impersonation checks",
            "• Page title & favicon mismatch",
            "• Hidden redirection patterns",
            "• DOM tree structural markers"
        ], RED_ALERT)
    ]

    l_w = Inches(2.7)
    l_gap = Inches(0.3)
    for i, (title, points, col) in enumerate(layers):
        x = Inches(0.8) + i * (l_w + l_gap)
        card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.6), l_w, Inches(5.3))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = col
        tf = card.text_frame
        tf.word_wrap = True
        
        p_h = tf.paragraphs[0]
        p_h.text = title
        p_h.font.size = Pt(15)
        p_h.font.bold = True
        p_h.font.color.rgb = col
        
        for pt in points:
            p = tf.add_paragraph()
            p.text = pt
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_WHITE
            p.space_before = Pt(8)

    # -------------------------------------------------------------
    # SLIDE 7: KEY INNOVATION
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    set_bg(s7)
    add_header(s7, "Key Innovation: Progressive Low-Latency Detection", "06 / INNOVATION")

    # Comparison Columns: Traditional vs Our Approach
    c_trad = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.7), Inches(3.2))
    c_trad.fill.solid()
    c_trad.fill.fore_color.rgb = CARD_BG
    c_trad.line.color.rgb = CARD_BORDER
    tf_tr = c_trad.text_frame
    tf_tr.word_wrap = True
    ptr_h = tf_tr.paragraphs[0]
    ptr_h.text = "TRADITIONAL DETECTION APPROACH"
    ptr_h.font.size = Pt(13)
    ptr_h.font.bold = True
    ptr_h.font.color.rgb = TEXT_MUTED

    ptr_flow = tf_tr.add_paragraph()
    ptr_flow.text = "Every URL  ➔  Deep Analysis  ➔  High Processing & Latency"
    ptr_flow.font.size = Pt(13)
    ptr_flow.font.bold = True
    ptr_flow.font.color.rgb = RED_ALERT
    ptr_flow.space_before = Pt(8)

    ptr_desc = tf_tr.add_paragraph()
    ptr_desc.text = "Runs heavy analysis or queries external clouds on every single website. This introduces browser lag, increases server infrastructure costs, and harms user browsing speeds."
    ptr_desc.font.size = Pt(11)
    ptr_desc.font.color.rgb = TEXT_MUTED
    ptr_desc.space_before = Pt(10)

    c_ours = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(3.2))
    c_ours.fill.solid()
    c_ours.fill.fore_color.rgb = CARD_BG
    c_ours.line.color.rgb = ACCENT_CYAN
    tf_ou = c_ours.text_frame
    tf_ou.word_wrap = True
    pou_h = tf_ou.paragraphs[0]
    pou_h.text = "OUR PROGRESSIVE APPROACH"
    pou_h.font.size = Pt(13)
    pou_h.font.bold = True
    pou_h.font.color.rgb = ACCENT_CYAN

    pou_flow = tf_ou.add_paragraph()
    pou_flow.text = "Every URL  ➔  Fast Local Check  ➔  Safe? Allow (<10ms)\n                                                  ↓\n                                  Suspicious/Unknown  ➔  Deep Analysis"
    pou_flow.font.size = Pt(12)
    pou_flow.font.bold = True
    pou_flow.font.color.rgb = GREEN_SAFE
    pou_flow.space_before = Pt(8)

    # Explanation Banner + 4 Key Benefits
    bot_card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.1), Inches(11.7), Inches(1.8))
    bot_card.fill.solid()
    bot_card.fill.fore_color.rgb = RGBColor(16, 42, 77)
    bot_card.line.color.rgb = CARD_BORDER
    tf_bot = bot_card.text_frame
    tf_bot.word_wrap = True
    
    pb_h = tf_bot.paragraphs[0]
    pb_h.text = "“The system does not perform expensive analysis on every website. It progressively increases the depth of analysis only when necessary.”"
    pb_h.font.size = Pt(13)
    pb_h.font.bold = True
    pb_h.font.color.rgb = TEXT_WHITE
    
    pb_pts = tf_bot.add_paragraph()
    pb_pts.text = "✔ Faster Response Times     ✔ Reduced Unnecessary Processing     ✔ Detection of Unknown Threats     ✔ Explainable Risk Assessment"
    pb_pts.font.size = Pt(12)
    pb_pts.font.color.rgb = ACCENT_CYAN
    pb_pts.space_before = Pt(8)

    # -------------------------------------------------------------
    # SLIDE 8: USER EXPERIENCE (3 WARNING STATES)
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    set_bg(s8)
    add_header(s8, "User Experience: Clean & Actionable Security Alerts", "07 / USER EXPERIENCE")

    ux_states = [
        ("🟢 SAFE", GREEN_SAFE, "Normal Browsing Allowed", "“No significant phishing indicators detected.”", "• Known trusted domain\n• Clean SSL & DNS records\n• Standard URL structure\n\nExperience: 0ms added delay.", "[VISITING SITE]"),
        ("🟡 SUSPICIOUS", YELLOW_WARN, "Caution Recommended", "“Unknown domain with suspicious characteristics.”", "• Newly registered domain\n• Domain reputation unavailable\n• Minor structural anomalies\n\nAction: Extra caution advised.", "[GO BACK]  [CONTINUE]"),
        ("🔴 HIGH RISK", RED_ALERT, "Phishing Attack Detected", "“Possible phishing website detected.”", "Reasons:\n• Suspicious domain structure\n• Brand impersonation detected\n• Suspicious login form detected\n\nAction: Immediate user protection.", "[LEAVE WEBSITE (RECOMMENDED)]")
    ]

    u_w = Inches(3.7)
    u_gap = Inches(0.3)
    for i, (tag, col, sub, quote, details, buttons) in enumerate(ux_states):
        x = Inches(0.8) + i * (u_w + u_gap)
        card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.6), u_w, Inches(5.3))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = col
        tf = card.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = tag
        p_t.font.size = Pt(20)
        p_t.font.bold = True
        p_t.font.color.rgb = col
        
        p_sub = tf.add_paragraph()
        p_sub.text = sub
        p_sub.font.size = Pt(13)
        p_sub.font.bold = True
        p_sub.font.color.rgb = TEXT_WHITE
        p_sub.space_before = Pt(4)
        
        p_q = tf.add_paragraph()
        p_q.text = quote
        p_q.font.size = Pt(12)
        p_q.font.color.rgb = ACCENT_CYAN if col != RED_ALERT else ROSE
        p_q.space_before = Pt(10)
        
        p_det = tf.add_paragraph()
        p_det.text = details
        p_det.font.size = Pt(11)
        p_det.font.color.rgb = TEXT_MUTED
        p_det.space_before = Pt(12)
        
        p_btn = tf.add_paragraph()
        p_btn.text = buttons
        p_btn.font.size = Pt(12)
        p_btn.font.bold = True
        p_btn.font.color.rgb = col
        p_btn.space_before = Pt(20)

    # -------------------------------------------------------------
    # SLIDE 9: TECHNOLOGY & ARCHITECTURE
    # -------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    set_bg(s9)
    add_header(s9, "System Architecture & Technology Stack", "08 / ARCHITECTURE")

    # Left: Architecture Flow (Simple Vertical/Horizontal boxes)
    card_arch = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3))
    card_arch.fill.solid()
    card_arch.fill.fore_color.rgb = CARD_BG
    card_arch.line.color.rgb = ACCENT_CYAN
    tf_arch = card_arch.text_frame
    tf_arch.word_wrap = True
    par_h = tf_arch.paragraphs[0]
    par_h.text = "SIMPLE SYSTEM ARCHITECTURE"
    par_h.font.size = Pt(15)
    par_h.font.bold = True
    par_h.font.color.rgb = ACCENT_CYAN

    arch_flow = [
        "Browser Extension (Chrome / Edge)",
        "Local Detection Engine (On-Device Heuristics)",
        "Backend API (FastAPI / Python Service)",
        "Threat Intelligence Database & Cache",
        "Machine Learning Model (Zero-Day Detection)",
        "Risk Engine (Risk Score Aggregator)",
        "Browser Warning UI (Safe / Warn / Block)"
    ]
    for idx, step in enumerate(arch_flow):
        p = tf_arch.add_paragraph()
        arrow = "↓ " if idx < len(arch_flow) - 1 else "★ "
        p.text = f"{arrow}{step}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_before = Pt(6)

    # Right: Pragmatic Tech Stack Categories
    techs = [
        ("Frontend / Extension", "Chrome / Edge Extension APIs, Manifest V3, JavaScript / TypeScript"),
        ("Backend Services", "Python, FastAPI (Asynchronous & Lightweight API Framework)"),
        ("Data Storage & Caching", "PostgreSQL (Threat intelligence & telemetry), Redis (Fast hash lookups)"),
        ("Machine Learning", "Lightweight ML Model (Classifier for zero-day URL/DOM patterns)"),
        ("Threat & Domain Services", "Threat-intelligence APIs, DNS resolution & domain intelligence services")
    ]

    card_tech = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3))
    card_tech.fill.solid()
    card_tech.fill.fore_color.rgb = CARD_BG
    card_tech.line.color.rgb = CARD_BORDER
    tf_tech = card_tech.text_frame
    tf_tech.word_wrap = True
    ptc_h = tf_tech.paragraphs[0]
    ptc_h.text = "TECHNOLOGY STACK"
    ptc_h.font.size = Pt(15)
    ptc_h.font.bold = True
    ptc_h.font.color.rgb = ACCENT_CYAN

    for cat, items in techs:
        p = tf_tech.add_paragraph()
        p.text = f"• {cat}:"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_before = Pt(8)
        
        pi = tf_tech.add_paragraph()
        pi.text = f"  {items}"
        pi.font.size = Pt(11)
        pi.font.color.rgb = TEXT_MUTED
        pi.space_before = Pt(2)

    # -------------------------------------------------------------
    # SLIDE 10: IMPACT & FUTURE SCOPE
    # -------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    set_bg(s10)
    add_header(s10, "Impact, Future Scope & Vision", "09 / IMPACT & ROADMAP")

    # Left: Impact Card
    card_imp = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.7), Inches(3.8))
    card_imp.fill.solid()
    card_imp.fill.fore_color.rgb = CARD_BG
    card_imp.line.color.rgb = GREEN_SAFE
    tf_imp = card_imp.text_frame
    tf_imp.word_wrap = True
    pim_h = tf_imp.paragraphs[0]
    pim_h.text = "PROJECT IMPACT"
    pim_h.font.size = Pt(16)
    pim_h.font.bold = True
    pim_h.font.color.rgb = GREEN_SAFE

    impact_points = [
        "✔ Protect Users from Phishing in real time before data submission",
        "✔ Detect Previously Unseen Threats without waiting for database updates",
        "✔ Reduce Detection Latency with fast on-device pre-checks",
        "✔ Explain Why a Website is Suspicious with transparent indicators",
        "✔ Reduce Unnecessary Deep Analysis by filtering safe sites early"
    ]
    for pt in impact_points:
        p = tf_imp.add_paragraph()
        p.text = pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_WHITE
        p.space_before = Pt(8)

    # Right: Future Scope Card
    card_fut = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(3.8))
    card_fut.fill.solid()
    card_fut.fill.fore_color.rgb = CARD_BG
    card_fut.line.color.rgb = ACCENT_CYAN
    tf_fut = card_fut.text_frame
    tf_fut.word_wrap = True
    pfu_h = tf_fut.paragraphs[0]
    pfu_h.text = "FUTURE SCOPE & EXTENSIONS"
    pfu_h.font.size = Pt(16)
    pfu_h.font.bold = True
    pfu_h.font.color.rgb = ACCENT_CYAN

    future_points = [
        "📱 Mobile Browser Support (Android / iOS extension integrations)",
        "✉️ Email and SMS Phishing (Smishing) Detection modules",
        "📷 QR-Code Phishing (Quishing) detection in web links",
        "🌐 Multilingual Scam Detection tailored for regional languages",
        "🧠 Continuously Improved ML Models with federated edge learning",
        "🏢 Organization-Level Security Dashboard for IT administrators"
    ]
    for pt in future_points:
        p = tf_fut.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_before = Pt(6)

    # Bottom Tagline Banner
    tag_box = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.6), Inches(11.7), Inches(1.3))
    tag_box.fill.solid()
    tag_box.fill.fore_color.rgb = RGBColor(16, 42, 77)
    tag_box.line.color.rgb = ACCENT_CYAN
    tf_tag = tag_box.text_frame
    tf_tag.word_wrap = True
    
    ptag = tf_tag.paragraphs[0]
    ptag.text = "“Detect early. Analyze intelligently. Protect users in real time.”"
    ptag.font.size = Pt(18)
    ptag.font.bold = True
    ptag.font.color.rgb = ACCENT_CYAN
    ptag.alignment = PP_ALIGN.CENTER
    
    ptag_sub = tf_tag.add_paragraph()
    ptag_sub.text = "Thank you! Open for Questions & Demonstration."
    ptag_sub.font.size = Pt(12)
    ptag_sub.font.color.rgb = TEXT_WHITE
    ptag_sub.alignment = PP_ALIGN.CENTER
    ptag_sub.space_before = Pt(4)

    # Save SIH presentation
    output_path = r"e:\INSTA AUTOMATION\SIH_PhishGuard_Presentation.pptx"
    prs.save(output_path)
    print(f"SIH Presentation successfully saved to: {output_path}")

if __name__ == "__main__":
    build_sih_presentation()
