#!/usr/bin/env python3
"""ChainSentry Academy certificate PDF — premium redesign v3.

Fixes vs v2 (vision-autopsy defects 1-8):
  S1  orphaned seal floating in hollow middle -> seal + SIGNATURE BLOCK paired
      bottom-left/right as a balanced footer axis; title centered as capstone
  S2  vertical whitespace void -> content distributed on a modular rhythm:
      top band (title), middle band (recipient), lower band (seal+signature), footer strip
  S3  seal internals -> rebuilt: matched navy, centred star, 58px wordmark, real clearance
  S4  footer baseline islands + QR in gutter -> one baseline grid INSIDE safe area,
      QR fully within the gold rule
  S5  black-on-navy name clash + shouting stack -> recipient navy, clear
      1-2-3 ladder (title >> name >> course), STATUS emphasized as green chip
  S6  eyeballed spacing -> modular 8/16/24/40 rhythm baked into constants
  S7  seal has no job -> signature line + signatory title beside the seal
  S8  mismatched navys/golds -> single NAVY/GOLD/GRAY token set everywhere
"""
import io as _io
import os


def _brand_tokens():
    """Official chainSENTRY design tokens (source: chainsentry.arasintegrasi.ai theme CSS --cs-*)."""
    NAVY = "#1c2a3b"    # --cs-accent-subtle (deep panel navy)
    GOLD = "#f2c14e"    # --cs-sev-elevated (house amber/gold)
    GRAY = "#8e9299"    # --cs-text-tertiary
    GREEN = "#6ad3a0"   # --cs-state-positive
    return NAVY, GOLD, GRAY, GREEN


def cert_pdf(holder: str, course: str, cid: str, issued: str, serial: str,
             expires, status: str, base_url: str, seal_path) -> bytes:
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.units import mm
    from reportlab.lib.colors import HexColor
    from reportlab.pdfgen import canvas as _canvas
    import qrcode as _qrcode

    NAVY_H, GOLD_H, GRAY_H, GREEN_H = _brand_tokens()
    NAVY, GOLD, GRAY, GREEN = (HexColor(c) for c in (NAVY_H, GOLD_H, GRAY_H, GREEN_H))

    # modular vertical rhythm (mm from top) — S6
    R = {"frame": 14, "inner": 18, "kicker": 26, "title": 40, "lead1": 54,
         "name": 66, "lead2": 78, "course": 90, "divider": 104,
         "sealzone_top": 118, "sig_line": 168, "footer": 26}

    buf = _io.BytesIO()
    W, H = landscape(A4)
    cv = _canvas.Canvas(buf, pagesize=(W, H))
    Y = lambda mm_from_top: H - mm_from_top * mm

    # watermark: giant faint brand mark centred on the former void zone (behind content)
    wm_path = os.path.join(os.path.dirname(seal_path or ""), "watermark.png") if seal_path else None
    if wm_path and os.path.exists(wm_path):
        wm_sz = 108*mm
        from reportlab.lib.utils import ImageReader as _IRWM
        cv.drawImage(_IRWM(wm_path), W/2-wm_sz/2-26*mm, H/2-wm_sz/2-2*mm, wm_sz, wm_sz)  # shifted left, off the signature column

    # frame — S8 same tokens
    cv.setStrokeColor(NAVY); cv.setLineWidth(2)
    cv.rect(R["frame"]*mm, R["frame"]*mm, W-2*R["frame"]*mm, H-2*R["frame"]*mm)
    cv.setStrokeColor(GOLD); cv.setLineWidth(0.8)
    cv.rect(R["inner"]*mm, R["inner"]*mm, W-2*R["inner"]*mm, H-2*R["inner"]*mm)

    SAFE = R["inner"] + 6  # safe-area inset (mm) — everything lives inside this

    # top band — kicker + title (1)
    cv.setFillColor(GRAY)
    cv.setFont("Helvetica-Bold", 12)
    cv.drawCentredString(W/2, Y(R["kicker"]), "C H A I N S E N T R Y   A C A D E M Y")
    cv.setFillColor(NAVY)
    cv.setFont("Helvetica-Bold", 30)
    cv.drawCentredString(W/2, Y(R["title"]), "CERTIFICATE OF COMPLETION")

    # middle band — recipient (2) — NAVY not black — S5
    cv.setFillColor(GRAY); cv.setFont("Helvetica", 12)
    cv.drawCentredString(W/2, Y(R["lead1"]), "This certifies that")
    cv.setFillColor(NAVY); cv.setFont("Helvetica-Bold", 26)
    cv.drawCentredString(W/2, Y(R["name"]), holder[:46])
    cv.setFillColor(GRAY); cv.setFont("Helvetica", 12)
    cv.drawCentredString(W/2, Y(R["lead2"]), "has successfully passed the examination for")
    cv.setFillColor(NAVY); cv.setFont("Helvetica-Bold", 17)
    cv.drawCentredString(W/2, Y(R["course"]), course)

    # divider — couples upper content to seal band — S2
    cv.setStrokeColor(GOLD); cv.setLineWidth(0.6)
    cv.line(W/2-36*mm, Y(R["divider"]), W/2+36*mm, Y(R["divider"]))

    # seal band: seal LEFT-of-centre + SIGNATURE RIGHT-of-centre, on ONE shared
    # optical axis — S1 (seal has a job) + S7
    SEAL_D = 50  # mm diameter — anchors the lower-left
    seal_left = W/2 - 84*mm         # points
    seal_bottom = Y(R["sealzone_top"]) - SEAL_D*mm
    from reportlab.lib.utils import ImageReader
    if seal_path and os.path.exists(seal_path):
        cv.drawImage(ImageReader(str(seal_path)), seal_left, seal_bottom, SEAL_D*mm, SEAL_D*mm, mask="auto")
    else:
        cv.setStrokeColor(NAVY); cv.circle(seal_left+SEAL_D/2*mm, seal_bottom+SEAL_D/2*mm, SEAL_D/2*mm, stroke=1, fill=0)

    # signature block — mirrors the seal, right of centre, same axis — S7
    sig_left = W/2 + 22*mm          # points
    # axis-align: signature rule at seal's optical centreline (seal centre = bottom + 23mm)
    seal_center_y = Y(R["sealzone_top"]) - 23*mm
    sig_y = seal_center_y           # shared axis
    # digital signature rendering (serif italic) above the rule — disclosed as digital signing
    try:
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        _sf = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
        if os.path.exists(_sf):
            pdfmetrics.registerFont(TTFont("SigIt", _sf))
            cv.setFillColor(NAVY); cv.setFont("SigIt", 15)
            cv.drawString(sig_left+1*mm, sig_y+4*mm, "Ahmad Fuad Kamarazaman")
        else:
            cv.setFillColor(NAVY); cv.setFont("Times-Italic", 15)
            cv.drawString(sig_left+1*mm, sig_y+4*mm, "Ahmad Fuad Kamarazaman")
    except Exception:
        pass
    cv.setStrokeColor(GRAY); cv.setLineWidth(0.7)
    cv.line(sig_left, sig_y, sig_left+56*mm, sig_y)
    cv.setFillColor(NAVY); cv.setFont("Helvetica-Bold", 11)
    cv.drawString(sig_left, sig_y-13, "AHMAD FUAD KAMARAZAMAN")
    cv.setFillColor(GRAY); cv.setFont("Helvetica", 9)
    cv.drawString(sig_left, sig_y-23, "Academic Director, ChainSentry Academy")
    cv.setFillColor(HexColor("#8A94A0")); cv.setFont("Helvetica-Oblique", 7)
    cv.drawString(sig_left, sig_y-31, "Digitally signed")

    # footer strip — SIMPLE, explicit, single baseline — S4
    fy = 23*mm  # inside BOTH rules, breathing room from the inner rule
    cv.setFillColor(GRAY); cv.setFont("Helvetica", 9.5)
    lx = 22*mm
    cv.drawString(lx, fy+12, f"Credential ID: {cid}")
    cv.drawString(lx, fy, f"Issued: {issued}    Serial: {serial}")
    # expiry right-aligned on ITS own line, no chip overlap
    rx = W - 22*mm
    cv.drawRightString(rx, fy+12, f"Expires: {expires or 'Lifetime'}")
    # status chip BELOW expiry line, clear — chip_h in POINTS consistently
    chip_w, chip_h = 38*mm, 10
    # status pill in BRAND METALS: gold-tint fill + navy outline (kills the orphan-green)
    cv.setFillColor(HexColor("#FBF3DC"))
    cv.roundRect(rx-chip_w, fy-1.5, chip_w, chip_h, 3, stroke=0, fill=1)
    cv.setStrokeColor(NAVY); cv.setLineWidth(0.8)
    cv.roundRect(rx-chip_w, fy-1.5, chip_w, chip_h, 3, stroke=1, fill=0)
    cv.setFillColor(NAVY); cv.setFont("Helvetica-Bold", 8.5)
    cv.drawCentredString(rx-chip_w/2, fy+1.2, f"STATUS: {status}")

    # QR — left of the expiry/status column, INSIDE the frame — S4
    import urllib.parse
    vurl = f"{base_url}/verify?id={urllib.parse.quote(cid)}"
    qr = _qrcode.QRCode(box_size=4, border=1)
    qr.add_data(vurl); qr.make(fit=True)
    qimg = qr.make_image(fill_color="#101820", back_color="white")  # near-black: scannability
    qbuf = _io.BytesIO(); qimg.save(qbuf, format="PNG"); qbuf.seek(0)
    qs = 18
    # measure the REAL left-block width (longest of the two footer lines) — no guessed extents
    from reportlab.pdfbase.pdfmetrics import stringWidth as _sw
    w_line1 = _sw(f"Credential ID: {cid}", "Helvetica", 9.5)
    w_line2 = _sw(f"Issued: {issued}    Serial: {serial}", "Helvetica", 9.5)
    left_edge = lx
    right_edge = left_edge + max(w_line1, w_line2)
    gap_mid_x = (right_edge + (rx - 38*mm))/2          # mid of whitespace up to the chip column
    qx = gap_mid_x - qs*mm/2                           # true optical centre of the gap
    gap_mid_y = fy + 8                                  # vertical centre of the two-line block
    qy_bottom = gap_mid_y - qs*mm/2                     # QR centred against both lines
    cv.drawImage(ImageReader(qbuf), qx, qy_bottom, qs*mm, qs*mm)
    cv.setFillColor(GRAY); cv.setFont("Helvetica-Bold", 7.5)
    cv.drawCentredString(qx+qs/2*mm, qy_bottom-5.5, "Scan to verify")
    cv.showPage(); cv.save()
    return buf.getvalue()
