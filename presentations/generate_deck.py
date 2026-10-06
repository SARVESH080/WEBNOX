import collections.abc
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette (Dark Theme / Cybersecurity)
    BG_COLOR = RGBColor(15, 23, 42)        # Slate 900 #0F172A
    CARD_BG = RGBColor(30, 41, 59)         # Slate 800 #1E293B
    CARD_BORDER = RGBColor(51, 65, 85)     # Slate 700
    ACCENT_CYAN = RGBColor(56, 189, 248)   # Sky 400 #38BDF8
    TEXT_WHITE = RGBColor(248, 250, 252)   # Slate 50
    TEXT_MUTED = RGBColor(148, 163, 184)   # Slate 400
    EMERALD = RGBColor(52, 211, 153)       # Emerald 400
    AMBER = RGBColor(251, 191, 36)         # Amber 400
    ROSE = RGBColor(251, 113, 133)         # Rose 400

    def apply_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category="PHISHGUARD ARCHITECTURE"):
        # Category label
        tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.5), Inches(0.4))
        p_cat = tb_cat.text_frame.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_CYAN
        
        # Main Title
        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.5), Inches(0.7))
        p_title = tb_title.text_frame.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE

    # -------------------------------------------------------------
    # SLIDE 1: Title Slide
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    apply_bg(s1)
    
    # Title badge
    badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(3.2), Inches(0.4))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(30, 58, 138)
    badge.line.color.rgb = ACCENT_CYAN
    p_b = badge.text_frame.paragraphs[0]
    p_b.text = "REAL-TIME CYBERSECURITY"
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_CYAN
    p_b.alignment = PP_ALIGN.CENTER

    tb_main = s1.shapes.add_textbox(Inches(0.8), Inches(2.4), Inches(11.5), Inches(2.2))
    tf_main = tb_main.text_frame
    tf_main.word_wrap = True
    p1 = tf_main.paragraphs[0]
    p1.text = "PhishGuard"
    p1.font.size = Pt(54)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE

    p2 = tf_main.add_paragraph()
    p2.text = "Progressive Real-Time Phishing Detection with Sub-50ms Risk Analysis"
    p2.font.size = Pt(22)
    p2.font.color.rgb = ACCENT_CYAN
    p2.space_before = Pt(10)

    p3 = tf_main.add_paragraph()
    p3.text = "Eliminating the critical zero-day threat window with hybrid edge-cloud intelligence."
    p3.font.size = Pt(15)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(10)

    # Presenter card
    card_pres = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.2), Inches(11.7), Inches(1.3))
    card_pres.fill.solid()
    card_pres.fill.fore_color.rgb = CARD_BG
    card_pres.line.color.rgb = CARD_BORDER
    tf_p = card_pres.text_frame
    tf_p.word_wrap = True
    p_pr1 = tf_p.paragraphs[0]
    p_pr1.text = "Hackathon Pitch Deck | Track: Cybersecurity & AI / Browser Engineering"
    p_pr1.font.size = Pt(13)
    p_pr1.font.bold = True
    p_pr1.font.color.rgb = TEXT_WHITE
    p_pr2 = tf_p.add_paragraph()
    p_pr2.text = "Presented by Team PhishGuard"
    p_pr2.font.size = Pt(12)
    p_pr2.font.color.rgb = ACCENT_CYAN
    p_pr2.space_before = Pt(4)

    # -------------------------------------------------------------
    # SLIDE 2: Problem Statement
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    apply_bg(s2)
    add_header(s2, "The Critical Zero-Day Blindspot in Modern Phishing", "01 / THE PROBLEM")

    cards_data = [
        ("The 4-Hour Life Cycle", "Modern phishing attacks are spun up and torn down in under 4 hours. By the time threat-intelligence databases index them, 90%+ of credentials have already been stolen.", ROSE),
        ("The Cloud Latency Dilemma", "Deep cloud sandboxing and backend re-crawling introduces 2-4 seconds of lag per link. Users experience annoying delays and frequently disable security tools.", AMBER),
        ("'Living off the Land' Tactics", "Attackers host scams on legitimate platforms (firebaseapp.com, docs.google.com, vercel.app). Domain reputation checks fail completely because the root domain is trusted.", ACCENT_CYAN)
    ]

    for i, (title, desc, color) in enumerate(cards_data):
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i * 4.0), Inches(1.8), Inches(3.7), Inches(4.8))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color
        tf = card.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = f"0{i+1}"
        p_t.font.size = Pt(28)
        p_t.font.bold = True
        p_t.font.color.rgb = color
        
        p_head = tf.add_paragraph()
        p_head.text = title
        p_head.font.size = Pt(18)
        p_head.font.bold = True
        p_head.font.color.rgb = TEXT_WHITE
        p_head.space_before = Pt(10)
        
        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(13)
        p_desc.font.color.rgb = TEXT_MUTED
        p_desc.space_before = Pt(14)

    # -------------------------------------------------------------
    # SLIDE 3: Existing Solutions vs PhishGuard
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    apply_bg(s3)
    add_header(s3, "Competitive Analysis: The Speed vs. Detection Dilemma", "02 / COMPETITIVE LANDSCAPE")

    # Table layout
    rows, cols = 4, 4
    table_shape = s3.shapes.add_table(rows, cols, Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.5))
    table = table_shape.table
    
    table.columns[0].width = Inches(3.2)
    table.columns[1].width = Inches(2.8)
    table.columns[2].width = Inches(2.8)
    table.columns[3].width = Inches(2.9)

    headers = ["Evaluation Criteria", "Google Safe Browsing", "Enterprise Cloud Proxies", "PhishGuard (Our Solution)"]
    data = [
        ["Zero-Day Threat Detection", "POOR (Feeds lag by 2-8h)", "HIGH (Heavy deep analysis)", "HIGH (Instant real-time ML)"],
        ["User Latency Overhead", "< 50 ms (Local Hash list)", "SLOW (2,000 - 4,000 ms)", "< 50 ms (Progressive Triage)"],
        ["Privacy / Data Leaks", "HIGH (k-Anonymity hashes)", "LOW (Logs full browsing URLs)", "HIGH (Zero-leakage Vectors)"]
    ]

    for col_idx, text in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(30, 58, 138) if col_idx == 3 else RGBColor(51, 65, 85)
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN if col_idx == 3 else TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER

    for row_idx, row_data in enumerate(data):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(17, 24, 39) if col_idx == 3 else CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.text = text
            p.font.size = Pt(12)
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT
            if col_idx == 3:
                p.font.bold = True
                p.font.color.rgb = EMERALD
            else:
                p.font.color.rgb = TEXT_MUTED if col_idx == 0 else TEXT_WHITE

    # -------------------------------------------------------------
    # SLIDE 4: Proposed Solution - PhishGuard
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    apply_bg(s4)
    add_header(s4, "PhishGuard: Progressive Multi-Tier Defense Pipeline", "03 / THE SOLUTION")

    tiers = [
        ("Tier 1: On-Device Triage", "< 10 ms", "Local Bloom Filter checks top 50,000 safe domains in O(1) time. Evaluates lexical URL entropy, IP addresses, and homoglyphs. 90%+ benign traffic exits here with 0ms penalty.", EMERALD),
        ("Tier 2: DOM & Form Analysis", "< 30 ms", "In-browser content script detects password inputs on unknown hosts. Flags brand mismatches (e.g. PayPal logo on vercel.app) and foreign credential submission targets.", ACCENT_CYAN),
        ("Tier 3: Cloud Micro-Inference", "< 180 ms", "For amber-risk pages, extracts a 10-point numerical vector and queries our low-latency ML model. High-risk pages trigger an instant blocking screen.", AMBER)
    ]

    for i, (title, latency, desc, color) in enumerate(tiers):
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i * 4.0), Inches(1.8), Inches(3.7), Inches(4.8))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color
        tf = card.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = latency
        p_t.font.size = Pt(26)
        p_t.font.bold = True
        p_t.font.color.rgb = color
        
        p_head = tf.add_paragraph()
        p_head.text = title
        p_head.font.size = Pt(16)
        p_head.font.bold = True
        p_head.font.color.rgb = TEXT_WHITE
        p_head.space_before = Pt(8)
        
        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_MUTED
        p_desc.space_before = Pt(14)

    # -------------------------------------------------------------
    # SLIDE 5: Core Innovations
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    apply_bg(s5)
    add_header(s5, "Key Innovations: Solving the Unsolved Engineering Hurdles", "04 / INNOVATION")

    innovations = [
        ("Speculative Form Shielding", "Instead of blocking entire network traffic and causing latency, we instantly freeze only <input type='password'> elements with a micro-spinner the instant an unknown site loads. Users are protected before ML finishes.", ACCENT_CYAN),
        ("Edge Feature Extraction (Anti-Cloaking)", "Phishers use bot-detection to show clean pages to cloud scanners. PhishGuard extracts DOM features directly inside the user's browser, completely bypassing attacker cloaking techniques.", EMERALD),
        ("Zero-Leakage k-Anonymity Vectors", "We never send browsing URLs, reset tokens, or session IDs to our servers. Only 32-bit hash prefixes and anonymized numerical feature vectors are transmitted, guaranteeing enterprise GDPR compliance.", ROSE)
    ]

    for i, (title, desc, color) in enumerate(innovations):
        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8 + i * 1.65), Inches(11.7), Inches(1.4))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color
        tf = card.text_frame
        tf.word_wrap = True
        
        p_h = tf.paragraphs[0]
        p_h.text = title
        p_h.font.size = Pt(16)
        p_h.font.bold = True
        p_h.font.color.rgb = color
        
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_WHITE
        p_d.space_before = Pt(4)

    # -------------------------------------------------------------
    # SLIDE 6: System Architecture & Workflow
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    apply_bg(s6)
    add_header(s6, "End-to-End System Architecture & Data Flow", "05 / ARCHITECTURE")

    steps = [
        ("1. User Navigates", "User clicks/visits URL. Chrome webNavigation fires in background script.", CARD_BORDER),
        ("2. Local Bloom Filter", "Top 50k safe domains checked in O(1) time. Safe = instant exit (0ms).", EMERALD),
        ("3. DOM Inspector", "Content script checks password inputs, brand mismatches, and form actions.", AMBER),
        ("4. Vector Inference", "Lightweight vector sent to FastAPI backend. XGBoost outputs Risk Score.", ACCENT_CYAN),
        ("5. Enforcement", "Score > 75: Instant Red Screen Block. Score < 40: Unfreeze page.", ROSE)
    ]

    for i, (title, desc, color) in enumerate(steps):
        card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i * 2.4), Inches(2.2), Inches(2.2), Inches(4.0))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color
        tf = card.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE
        
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.space_before = Pt(10)

    # -------------------------------------------------------------
    # SLIDE 7: Tech Stack
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    apply_bg(s7)
    add_header(s7, "Production-Ready Technology Stack", "06 / TECH STACK")

    tech_components = [
        ("Browser Extension Client", "Manifest V3 Architecture\n• TypeScript / Modern JavaScript\n• Content Scripts for DOM Vectorization\n• Client-Side Bloom Filter (150 KB)\n• WebNavigation Event Listeners", ACCENT_CYAN),
        ("Low-Latency Backend API", "High-Throughput Microservice\n• Python FastAPI (Asynchronous ASGI)\n• Uvicorn Production Web Server\n• CORS & Pydantic Data Validation\n• Lightweight JSON Payload (< 200 bytes)", EMERALD),
        ("Machine Learning Engine", "Zero-Day Classifier\n• LightGBM / XGBoost Model (~2MB)\n• Features: URL entropy, brand-mismatch, subdomains, form targets\n• Sub-5ms inference per request\n• Trained on PhishTank & Tranco datasets", AMBER),
        ("Cloud Infrastructure", "Serverless & Edge Deployment\n• Render / Railway Web Service\n• Upstash Redis (Hash-Prefix Caching)\n• Auto-scaling cloud container\n• Zero-cost prototype architecture", ROSE)
    ]

    for i, (title, desc, color) in enumerate(tech_components):
        row = i // 2
        col = i % 2
        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + col * 6.0), Inches(1.8 + row * 2.5), Inches(5.7), Inches(2.2))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color
        tf = card.text_frame
        tf.word_wrap = True
        
        p_h = tf.paragraphs[0]
        p_h.text = title
        p_h.font.size = Pt(16)
        p_h.font.bold = True
        p_h.font.color.rgb = color
        
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_WHITE
        p_d.space_before = Pt(6)

    # -------------------------------------------------------------
    # SLIDE 8: Prototype Demo & Hackathon Benchmarks
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    apply_bg(s8)
    add_header(s8, "Prototype Demonstration & Hackathon Metrics", "07 / PROTOTYPE & TARGETS")

    # Left: Demo Walkthrough
    card_demo = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.8))
    card_demo.fill.solid()
    card_demo.fill.fore_color.rgb = CARD_BG
    card_demo.line.color.rgb = ACCENT_CYAN
    tf_demo = card_demo.text_frame
    tf_demo.word_wrap = True
    
    p_dm = tf_demo.paragraphs[0]
    p_dm.text = "Live Demo User Experience"
    p_dm.font.size = Pt(18)
    p_dm.font.bold = True
    p_dm.font.color.rgb = ACCENT_CYAN
    
    demo_points = [
        "🟢 Clean Site (e.g. Wikipedia): Local Bloom Filter hits. Badge shows 'Safe' in 0 ms.",
        "🟡 Unknown Login Page: Speculative Shield activates. Input frozen for ~120 ms during check.",
        "🔴 Cloned Phishing Site (e.g. Fake Google on vercel.app): Brand mismatch detected. Risk: 96/100. Instant full-screen blocking page."
    ]
    for pt in demo_points:
        p_pt = tf_demo.add_paragraph()
        p_pt.text = pt
        p_pt.font.size = Pt(13)
        p_pt.font.color.rgb = TEXT_WHITE
        p_pt.space_before = Pt(14)

    # Right: Measurable Targets
    card_metrics = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))
    card_metrics.fill.solid()
    card_metrics.fill.fore_color.rgb = CARD_BG
    card_metrics.line.color.rgb = EMERALD
    tf_m = card_metrics.text_frame
    tf_m.word_wrap = True
    
    p_mt = tf_m.paragraphs[0]
    p_mt.text = "Performance Targets"
    p_mt.font.size = Pt(18)
    p_mt.font.bold = True
    p_mt.font.color.rgb = EMERALD
    
    metric_points = [
        "⚡ Local Bloom Filter: < 10 ms",
        "⚡ DOM Heuristics & Feature Extraction: < 30 ms",
        "⚡ Cloud Vector Inference (FastAPI): < 180 ms",
        "🎯 False Positive Rate: < 0.5% on Tranco top 100k",
        "🔒 Privacy Overhead: 0 URLs logged (GDPR compliant)"
    ]
    for pt in metric_points:
        p_pt = tf_m.add_paragraph()
        p_pt.text = pt
        p_pt.font.size = Pt(13)
        p_pt.font.color.rgb = TEXT_WHITE
        p_pt.space_before = Pt(14)

    # Save presentation
    output_path = r"e:\INSTA AUTOMATION\PhishGuard_Hackathon_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_presentation()
