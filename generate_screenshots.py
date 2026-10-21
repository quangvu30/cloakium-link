#!/usr/bin/env python3
import os
import subprocess
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR = os.path.join(SCRIPT_DIR, "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

SVG_LOGO = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="22" height="22">
  <defs>
    <radialGradient id="f-bg" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#030712"/>
    </radialGradient>
    <linearGradient id="f-cyan" x1="10%" y1="0%" x2="90%" y2="90%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#0ea5e9"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="f-indigo" x1="10%" y1="0%" x2="90%" y2="90%">
      <stop offset="0%" stop-color="#818cf8"/>
      <stop offset="50%" stop-color="#6366f1"/>
      <stop offset="100%" stop-color="#581c87"/>
    </linearGradient>
    <linearGradient id="f-purple" x1="10%" y1="0%" x2="90%" y2="90%">
      <stop offset="0%" stop-color="#c084fc"/>
      <stop offset="50%" stop-color="#9333ea"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <radialGradient id="f-core" cx="35%" cy="33%" r="65%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#bae6fd"/>
      <stop offset="65%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#034870"/>
    </radialGradient>
  </defs>
  <rect width="32" height="32" rx="7.5" fill="url(#f-bg)"/>
  <g transform="translate(16, 16) scale(0.068)">
    <path d="M 0 -166 A 166 166 0 0 1 143.76 83 L -7.55 65.57 A 66 66 0 0 0 60.56 -26.24 Z" fill="url(#f-cyan)"/>
    <g transform="rotate(120)">
      <path d="M 0 -166 A 166 166 0 0 1 143.76 83 L -7.55 65.57 A 66 66 0 0 0 60.56 -26.24 Z" fill="url(#f-indigo)"/>
    </g>
    <g transform="rotate(240)">
      <path d="M 0 -166 A 166 166 0 0 1 143.76 83 L -7.55 65.57 A 66 66 0 0 0 60.56 -26.24 Z" fill="url(#f-purple)"/>
    </g>
    <circle cx="0" cy="0" r="70" fill="#030712" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="0" cy="0" r="54" fill="url(#f-core)"/>
  </g>
</svg>'''

BASE_STYLES = '''
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  width: 1280px;
  height: 800px;
  overflow: hidden;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background: #0b0f19;
  color: #f1f5f9;
  display: flex;
  flex-direction: column;
}

/* Chrome Header Mockup */
.store-header {
  height: 48px;
  background: linear-gradient(90deg, #090d16 0%, #151a2e 50%, #090d16 100%);
  border-bottom: 1px solid rgba(255,255,255,0.08);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
}
.header-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(56, 189, 248, 0.12);
  border: 1px solid rgba(56, 189, 248, 0.3);
  padding: 4px 12px;
  border-radius: 999px;
  font-size: 12.5px;
  font-weight: 600;
  color: #38bdf8;
}
.header-title {
  font-size: 15px;
  font-weight: 700;
  color: #ffffff;
  display: flex;
  align-items: center;
  gap: 10px;
}
.header-meta {
  font-size: 12px;
  color: #94a3b8;
  display: flex;
  align-items: center;
  gap: 14px;
}

/* Browser Frame */
.browser-shell {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: #141824;
  overflow: hidden;
}

.chrome-tabbar {
  height: 38px;
  background: #0f131f;
  display: flex;
  align-items: flex-end;
  padding: 0 12px;
  gap: 6px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}
.window-controls {
  display: flex;
  gap: 7px;
  margin-right: 12px;
  margin-bottom: 11px;
}
.win-dot {
  width: 11px;
  height: 11px;
  border-radius: 50%;
}
.win-dot.close { background: #ef4444; }
.win-dot.min { background: #f59e0b; }
.win-dot.max { background: #10b981; }

.chrome-tab {
  height: 30px;
  padding: 0 14px;
  background: #181d2d;
  color: #cbd5e1;
  font-size: 12px;
  border-radius: 7px 7px 0 0;
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 500;
  border-top: 2px solid #38bdf8;
}
.chrome-tab.secondary {
  background: transparent;
  color: #64748b;
  border-top: none;
}

.chrome-nav {
  height: 38px;
  background: #181d2d;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  display: flex;
  align-items: center;
  padding: 0 16px;
  gap: 12px;
}
.nav-arrows {
  color: #64748b;
  font-size: 14px;
  display: flex;
  gap: 10px;
}
.url-bar {
  flex: 1;
  height: 26px;
  background: #0f131f;
  border-radius: 6px;
  border: 1px solid rgba(255,255,255,0.08);
  display: flex;
  align-items: center;
  padding: 0 12px;
  font-size: 12px;
  color: #94a3b8;
  gap: 8px;
}
.url-bar .lock { color: #10b981; }
.url-bar .host { color: #f1f5f9; font-weight: 500; }

.ext-badge-active {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(56, 189, 248, 0.15);
  border: 1px solid rgba(56, 189, 248, 0.35);
  border-radius: 6px;
  padding: 3px 8px;
  font-size: 11px;
  font-weight: 600;
  color: #38bdf8;
}

/* Workspace */
.workspace {
  flex: 1;
  display: flex;
  height: calc(100% - 76px);
  overflow: hidden;
}

.web-area {
  flex: 1;
  background: #0d1117;
  border-right: 1px solid #232936;
  position: relative;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.side-panel {
  width: 440px;
  background: #12151e;
  display: flex;
  flex-direction: column;
  position: relative;
  border-left: 1px solid rgba(255,255,255,0.06);
}

.panel-appbar {
  height: 44px;
  border-bottom: 1px solid #222838;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 14px;
  background: #141824;
}
.brand-group {
  display: flex;
  align-items: center;
  gap: 8px;
}
.brand-name {
  font-size: 13.5px;
  font-weight: 700;
  color: #f8fafc;
}
.page-chip {
  background: rgba(34, 197, 94, 0.12);
  border: 1px solid rgba(34, 197, 94, 0.25);
  padding: 3px 10px;
  border-radius: 999px;
  font-size: 11px;
  color: #4ade80;
  display: flex;
  align-items: center;
  gap: 5px;
  font-weight: 500;
}
.dot-green { width: 6px; height: 6px; border-radius: 50%; background: #22c55e; }

.panel-tabbar {
  display: flex;
  background: #0f131f;
  border-bottom: 1px solid #222838;
  padding: 0 8px;
}
.tab-btn {
  padding: 9px 14px;
  font-size: 12px;
  font-weight: 600;
  color: #94a3b8;
  border-bottom: 2px solid transparent;
  display: flex;
  align-items: center;
  gap: 5px;
}
.tab-btn.active {
  color: #38bdf8;
  border-bottom-color: #38bdf8;
  background: rgba(56, 189, 248, 0.05);
}
.tab-badge {
  background: rgba(56, 189, 248, 0.2);
  color: #38bdf8;
  font-size: 10px;
  padding: 1px 6px;
  border-radius: 10px;
}

/* Common Chat / Thread Styles */
.thread {
  flex: 1;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  overflow-y: hidden;
}
.msg {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.msg.user {
  align-items: flex-end;
}
.msg-role {
  font-size: 11px;
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.msg.user .msg-body {
  background: #1e293b;
  border: 1px solid #334155;
  color: #f8fafc;
  padding: 8px 12px;
  border-radius: 10px 10px 2px 10px;
  font-size: 12.5px;
  max-width: 90%;
  line-height: 1.45;
}
.msg.assistant .msg-body {
  background: #161b2a;
  border: 1px solid #283147;
  color: #e2e8f0;
  padding: 10px 12px;
  border-radius: 10px 10px 10px 2px;
  font-size: 12.5px;
  line-height: 1.45;
}

/* Thought card */
.think-card {
  border: 1px solid rgba(99, 102, 241, 0.3);
  background: rgba(99, 102, 241, 0.08);
  border-radius: 8px;
  padding: 8px 10px;
  font-size: 11.5px;
  color: #a5b4fc;
}
.think-header {
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
  color: #c7d2fe;
}

/* Tool execution card */
.tool-card {
  border: 1px solid rgba(56, 189, 248, 0.25);
  background: rgba(56, 189, 248, 0.05);
  border-radius: 7px;
  padding: 7px 10px;
  font-size: 11.5px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.tool-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 11px;
  color: #38bdf8;
  font-weight: 600;
}
.tool-status-ok {
  background: rgba(34, 197, 94, 0.15);
  color: #4ade80;
  padding: 1px 6px;
  border-radius: 4px;
  font-size: 10px;
}

/* Composer box */
.composer {
  padding: 10px;
  border-top: 1px solid #222838;
  background: #141824;
}
.composer-box {
  background: #0f131f;
  border: 1px solid #283147;
  border-radius: 8px;
  padding: 8px 10px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.composer-input {
  font-size: 12px;
  color: #94a3b8;
}
.composer-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.action-icons {
  display: flex;
  gap: 8px;
  color: #64748b;
  font-size: 13px;
}
.send-btn {
  background: #2563eb;
  color: white;
  border: none;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 11.5px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 4px;
}
'''

def render_html_to_png(html_content, output_name):
    tmp_html = f"/tmp/{output_name}.html"
    out_1280 = os.path.join(SCREENSHOTS_DIR, f"{output_name}-1280x800.png")
    out_640 = os.path.join(SCREENSHOTS_DIR, f"{output_name}-640x400.png")

    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Rendering 1280x800 for {output_name}...")
    subprocess.run([
        "google-chrome",
        "--headless=new",
        f"--screenshot={out_1280}",
        "--window-size=1280,800",
        "--hide-scrollbars",
        "--no-sandbox",
        "--font-render-hinting=max",
        f"file://{tmp_html}"
    ], check=True)

    print(f"Resizing to 640x400 for {output_name}...")
    with Image.open(out_1280) as im:
        im_resized = im.resize((640, 400), Image.Resampling.LANCZOS)
        im_resized.save(out_640, "PNG", optimize=True)

    print(f"✓ Saved: {out_1280} and {out_640}")

def generate_screenshot_1():
    html = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{BASE_STYLES}

/* Custom styling for left webpage (Automation demo) */
.demo-page {{
  padding: 28px 36px;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
  background: #0f172a;
}}
.demo-nav {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  padding-bottom: 16px;
}}
.demo-logo {{ font-size: 18px; font-weight: 800; color: #fff; display: flex; align-items: center; gap: 8px; }}
.demo-links {{ display: flex; gap: 20px; font-size: 13px; color: #94a3b8; }}

.demo-hero {{
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}}
.demo-hero h1 {{
  font-size: 32px;
  font-weight: 800;
  line-height: 1.2;
  color: #f8fafc;
}}
.demo-hero p {{
  font-size: 15px;
  color: #94a3b8;
  max-width: 580px;
  line-height: 1.5;
}}

.pricing-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
  margin-top: 10px;
}}
.price-card {{
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 12px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  position: relative;
}}
.price-card.featured {{
  border: 2px solid #38bdf8;
  background: #172554;
  box-shadow: 0 0 25px rgba(56, 189, 248, 0.15);
}}
.price-tag {{
  font-size: 26px;
  font-weight: 800;
  color: #fff;
}}

/* Simulated Agent Cursor on the webpage */
.agent-cursor {{
  position: absolute;
  top: 485px;
  left: 450px;
  z-index: 100;
  pointer-events: none;
}}
.cursor-dot {{
  width: 14px;
  height: 14px;
  background: #38bdf8;
  border: 2px solid #ffffff;
  border-radius: 50%;
  box-shadow: 0 0 12px #38bdf8;
}}
.cursor-label {{
  position: absolute;
  top: -24px;
  left: 18px;
  background: #0284c7;
  color: white;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
  white-space: nowrap;
}}

/* Simulated Screenshot Preview inside Assistant message */
.shot-preview {{
  margin-top: 8px;
  border-radius: 6px;
  border: 1px solid #38bdf8;
  overflow: hidden;
  background: #0f172a;
  padding: 6px;
}}
.shot-inner {{
  height: 70px;
  background: linear-gradient(135deg, #1e293b, #0f172a);
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #38bdf8;
  font-size: 11px;
  font-weight: 600;
  gap: 6px;
}}
</style>
</head>
<body>

  <!-- Top Header Banner for Chrome Web Store -->
  <div class="store-header">
    <div class="header-title">
      {SVG_LOGO}
      <span>Cloakium Link</span>
      <span style="color:#64748b; font-weight:400; font-size:13px;">| Chrome Extension</span>
    </div>
    <div class="header-badge">
      ⚡ AI Browser Agent — Automate Any Web Task
    </div>
    <div class="header-meta">
      <span>Manifest V3</span>
      <span>•</span>
      <span>Local LLM API Keys</span>
      <span>•</span>
      <span>CDP Trusted Inputs</span>
    </div>
  </div>

  <div class="browser-shell">
    <!-- Chrome Tabbar -->
    <div class="chrome-tabbar">
      <div class="window-controls">
        <div class="win-dot close"></div>
        <div class="win-dot min"></div>
        <div class="win-dot max"></div>
      </div>
      <div class="chrome-tab">
        <span>🌐 SaaS Pricing — Automate Flow</span>
      </div>
      <div class="chrome-tab secondary">
        <span>+ New Tab</span>
      </div>
    </div>

    <!-- Chrome Nav / URL bar -->
    <div class="chrome-nav">
      <div class="nav-arrows">
        <span>←</span>
        <span>→</span>
        <span>↻</span>
      </div>
      <div class="url-bar">
        <span class="lock">🔒</span>
        <span class="host">https://app.saasplatform.com</span>
        <span>/pricing</span>
      </div>
      <div class="ext-badge-active">
        {SVG_LOGO}
        <span>Side Panel Active</span>
      </div>
    </div>

    <!-- Workspace -->
    <div class="workspace">
      <!-- Webpage content -->
      <div class="web-area">
        <div class="demo-page">
          <div class="demo-nav">
            <div class="demo-logo">⚡ CloudDeploy</div>
            <div class="demo-links">
              <span>Features</span>
              <span>Integrations</span>
              <span style="color:#38bdf8; font-weight:600;">Pricing</span>
              <span>Documentation</span>
            </div>
          </div>

          <div class="demo-hero">
            <h1>Flexible plans for modern cloud teams</h1>
            <p>Deploy containers, serverless workflows, and real-time streaming with zero config overhead.</p>
          </div>

          <div class="pricing-grid">
            <div class="price-card">
              <h3 style="color:#cbd5e1; font-size:16px;">Starter Plan</h3>
              <div class="price-tag">$0 <span style="font-size:13px; color:#64748b; font-weight:400;">/ mo</span></div>
              <p style="font-size:12px; color:#94a3b8;">For individuals and rapid prototyping.</p>
              <button style="margin-top:auto; background:#334155; color:#cbd5e1; border:none; padding:8px; border-radius:6px; font-weight:600; font-size:12px;">Current Plan</button>
            </div>

            <div class="price-card featured" id="btn-pro-plan">
              <div style="position:absolute; top:-10px; right:16px; background:#38bdf8; color:#0f172a; font-size:10px; font-weight:800; padding:2px 8px; border-radius:12px;">POPULAR</div>
              <h3 style="color:#38bdf8; font-size:16px;">Pro Cloud Plan</h3>
              <div class="price-tag">$49 <span style="font-size:13px; color:#93c5fd; font-weight:400;">/ mo</span></div>
              <p style="font-size:12px; color:#cbd5e1;">Unlimited agents, high concurrency, and real-time telemetry.</p>
              <button style="margin-top:auto; background:#2563eb; color:white; border:none; padding:8px; border-radius:6px; font-weight:700; font-size:12px; box-shadow:0 0 15px rgba(37,99,235,0.5);">Upgrade to Pro</button>
            </div>
          </div>
        </div>

        <!-- Simulated AI Cursor -->
        <div class="agent-cursor">
          <div class="cursor-dot"></div>
          <div class="cursor-label">CDP simulate_mouse (isTrusted: true)</div>
        </div>
      </div>

      <!-- Extension Side Panel -->
      <div class="side-panel">
        <div class="panel-appbar">
          <div class="brand-group">
            {SVG_LOGO}
            <span class="brand-name">Cloakium Link</span>
          </div>
          <div class="page-chip">
            <span class="dot-green"></span>
            <span>CDP Attached</span>
          </div>
        </div>

        <div class="panel-tabbar">
          <div class="tab-btn active">Chat</div>
          <div class="tab-btn">Remote</div>
          <div class="tab-btn">Network <span class="tab-badge">14</span></div>
          <div class="tab-btn">Settings</div>
        </div>

        <div class="thread">
          <!-- User message -->
          <div class="msg user">
            <div class="msg-role">You</div>
            <div class="msg-body">
              Inspect the pricing plans, hover over the "Upgrade to Pro" button, and capture a screenshot.
            </div>
          </div>

          <!-- Assistant response with thought & tools -->
          <div class="msg assistant">
            <div class="msg-role">Cloakium Agent</div>
            <div class="msg-body">
              <div class="think-card">
                <div class="think-header">🧠 Reasoning</div>
                1. Queried DOM selector: <code>.price-card.featured button</code><br>
                2. Executing simulated mouse move along human curve.<br>
                3. Taking viewport screenshot via Chrome DevTools Protocol.
              </div>

              <div style="margin-top:8px;" class="tool-card">
                <div class="tool-title">
                  <span>▶ simulate_mouse (hover: #btn-pro-plan)</span>
                  <span class="tool-status-ok">18ms ✓</span>
                </div>
              </div>

              <div style="margin-top:6px;" class="tool-card">
                <div class="tool-title">
                  <span>▶ take_screenshot (clip: viewport)</span>
                  <span class="tool-status-ok">42ms ✓</span>
                </div>
              </div>

              <div class="shot-preview">
                <div class="shot-inner">
                  <span>📸 Captured Pro Plan Button (400x220px)</span>
                </div>
              </div>

              <p style="margin-top:8px;">Button hovered successfully with <code>isTrusted=true</code>. Screenshot captured above.</p>
            </div>
          </div>
        </div>

        <!-- Composer -->
        <div class="composer">
          <div class="composer-box">
            <div class="composer-input">
              Ask AI agent to click, fill forms, extract data or scrape...
            </div>
            <div class="composer-actions">
              <div class="action-icons">
                <span>🕒</span>
                <span>🎯 Pick</span>
                <span>＋</span>
              </div>
              <button class="send-btn">
                <span>Send</span>
                <span>↵</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</body>
</html>'''
    render_html_to_png(html, "screenshot-1-ai-agent")

def generate_screenshot_2():
    html = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{BASE_STYLES}

/* Remote LIVE Banner */
.remote-banner-live {{
  background: linear-gradient(90deg, #7f1d1d 0%, #991b1b 100%);
  border-bottom: 1px solid #ef4444;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  font-size: 12px;
  color: #fef2f2;
}}
.live-pulse {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
}}
.pulse-circle {{
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #ef4444;
  box-shadow: 0 0 10px #ef4444;
}}
.kick-btn {{
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.25);
  color: white;
  padding: 2px 10px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
}}

/* Web area simulation of remote stream */
.remote-stream-area {{
  flex: 1;
  background: #090d16;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 30px;
  position: relative;
}}
.stream-frame {{
  width: 90%;
  height: 85%;
  background: #111827;
  border: 2px dashed rgba(56, 189, 248, 0.4);
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  box-shadow: 0 0 40px rgba(0,0,0,0.6);
}}

/* Remote Tab Content in Side Panel */
.remote-view {{
  flex: 1;
  padding: 16px 14px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  overflow-y: hidden;
}}
.config-card {{
  background: #161b2a;
  border: 1px solid #283147;
  border-radius: 9px;
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}}
.card-header-title {{
  font-size: 12.5px;
  font-weight: 700;
  color: #f8fafc;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}
.card-desc {{
  font-size: 11.5px;
  color: #94a3b8;
  line-height: 1.4;
}}
.input-mock {{
  background: #0f131f;
  border: 1px solid #334155;
  border-radius: 6px;
  padding: 8px 10px;
  font-size: 12px;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  color: #38bdf8;
}}
.toggle-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 6px;
}}
.toggle-switch {{
  width: 38px;
  height: 20px;
  background: #2563eb;
  border-radius: 10px;
  position: relative;
}}
.toggle-knob {{
  width: 16px;
  height: 16px;
  background: white;
  border-radius: 50%;
  position: absolute;
  top: 2px;
  right: 2px;
}}
.badge-hash {{
  font-size: 10px;
  background: rgba(99, 102, 241, 0.15);
  color: #818cf8;
  border: 1px solid rgba(99, 102, 241, 0.3);
  padding: 2px 6px;
  border-radius: 4px;
}}
</style>
</head>
<body>

  <!-- Top Header Banner -->
  <div class="store-header">
    <div class="header-title">
      {SVG_LOGO}
      <span>Cloakium Link</span>
      <span style="color:#64748b; font-weight:400; font-size:13px;">| Peer-to-Peer Remote Control</span>
    </div>
    <div class="header-badge" style="background:rgba(239,68,68,0.15); border-color:rgba(239,68,68,0.3); color:#f87171;">
      🔴 WebRTC Direct Link & Telegram Bot
    </div>
    <div class="header-meta">
      <span>Zero Cloud Video Relaying</span>
      <span>•</span>
      <span>Argon2id Hash Protection</span>
      <span>•</span>
      <span>Sub-20ms Latency</span>
    </div>
  </div>

  <div class="browser-shell">
    <div class="chrome-tabbar">
      <div class="window-controls">
        <div class="win-dot close"></div>
        <div class="win-dot min"></div>
        <div class="win-dot max"></div>
      </div>
      <div class="chrome-tab">
        <span>🌐 Cloakium Web — Remote Session</span>
      </div>
    </div>

    <div class="chrome-nav">
      <div class="nav-arrows">
        <span>←</span>
        <span>→</span>
        <span>↻</span>
      </div>
      <div class="url-bar">
        <span class="lock">🔒</span>
        <span class="host">https://cloakium.site</span>
        <span>/dashboard/remote-chrome</span>
      </div>
      <div class="ext-badge-active" style="background:rgba(239,68,68,0.15); border-color:#ef4444; color:#f87171;">
        <span style="width:6px; height:6px; background:#ef4444; border-radius:50%;"></span>
        <span>LIVE CONTROL</span>
      </div>
    </div>

    <!-- Live indicator bar -->
    <div class="remote-banner-live">
      <div class="live-pulse">
        <div class="pulse-circle"></div>
        <span>LIVE: Remote browser session controlled from Cloakium (P2P WebRTC)</span>
      </div>
      <button class="kick-btn">Disconnect Session</button>
    </div>

    <div class="workspace">
      <!-- Web content: Stream area -->
      <div class="remote-stream-area">
        <div class="stream-frame">
          <div style="font-size:42px;">🖥️ ⇄ 🌐</div>
          <h2 style="font-size:20px; font-weight:700; color:#f8fafc;">Direct Peer-to-Peer Connection Active</h2>
          <p style="font-size:13px; color:#94a3b8; text-align:center; max-width:440px; line-height:1.5;">
            Mouse & keyboard events and high-FPS frames stream directly between your devices without storing images on servers.
          </p>
          <div style="display:flex; gap:12px; margin-top:8px;">
            <div style="background:#1e293b; border:1px solid #334155; padding:6px 12px; border-radius:6px; font-size:12px; color:#38bdf8;">
              ⚡ WebRTC Latency: <strong>12ms</strong>
            </div>
            <div style="background:#1e293b; border:1px solid #334155; padding:6px 12px; border-radius:6px; font-size:12px; color:#4ade80;">
              🔒 E2E Encrypted DataChannel
            </div>
          </div>
        </div>
      </div>

      <!-- Extension Side Panel -->
      <div class="side-panel">
        <div class="panel-appbar">
          <div class="brand-group">
            {SVG_LOGO}
            <span class="brand-name">Cloakium Link</span>
          </div>
          <div class="page-chip" style="background:rgba(239,68,68,0.15); border-color:rgba(239,68,68,0.3); color:#f87171;">
            <span style="width:6px; height:6px; background:#ef4444; border-radius:50%;"></span>
            <span>Remote Active</span>
          </div>
        </div>

        <div class="panel-tabbar">
          <div class="tab-btn">Chat</div>
          <div class="tab-btn active">Remote</div>
          <div class="tab-btn">Network</div>
          <div class="tab-btn">Settings</div>
        </div>

        <div class="remote-view">
          <!-- Pairing Card -->
          <div class="config-card">
            <div class="card-header-title">
              <span>Pairing Code (Mã ghép)</span>
              <span style="color:#4ade80; font-size:11px;">● Connected</span>
            </div>
            <div class="card-desc">Created in Cloakium → "My Chrome" tab.</div>
            <div class="input-mock">CLK-9842-SYNC</div>
          </div>

          <!-- Password Card -->
          <div class="config-card">
            <div class="card-header-title">
              <span>Access Password (Mật khẩu)</span>
              <span class="badge-hash">Argon2id Hash</span>
            </div>
            <div class="card-desc">Secured locally with salted Argon2id. Never sent plaintext.</div>
            <div class="input-mock">••••••••••••••••</div>
            <div class="toggle-row">
              <span style="font-size:12px; font-weight:600; color:#e2e8f0;">Allow Remote Control</span>
              <div class="toggle-switch">
                <div class="toggle-knob"></div>
              </div>
            </div>
          </div>

          <!-- Telegram Bot Card -->
          <div class="config-card">
            <div class="card-header-title">
              <span>Telegram Bot Integration</span>
              <span style="color:#38bdf8; font-size:11px;">Active</span>
            </div>
            <div class="card-desc">Send voice or text instructions to your Chrome via Telegram bot.</div>
            <div class="input-mock" style="color:#94a3b8;">@MyCloakiumAgentBot</div>
            <div style="font-size:11px; color:#4ade80;">✓ Authorized user: #81920381 (Admin)</div>
          </div>

          <div style="font-size:11px; color:#64748b; line-height:1.4; padding:0 4px;">
            ℹ️ When controlled remotely, Chrome displays its official security banner. You can terminate the session at any second.
          </div>
        </div>
      </div>
    </div>
  </div>

</body>
</html>'''
    render_html_to_png(html, "screenshot-2-remote-control")

def generate_screenshot_3():
    html = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{BASE_STYLES}

/* Settings view styles */
.settings-view {{
  flex: 1;
  padding: 14px 12px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  overflow-y: hidden;
}}

.provider-card {{
  background: #161b2a;
  border: 1px solid #283147;
  border-radius: 8px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}}

.provider-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
}}
.provider-name {{
  font-size: 13px;
  font-weight: 700;
  color: #f8fafc;
}}

.provider-tags {{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}}
.ptag {{
  background: #1e293b;
  border: 1px solid #334155;
  color: #94a3b8;
  font-size: 11px;
  padding: 3px 8px;
  border-radius: 5px;
}}
.ptag.active {{
  background: rgba(56, 189, 248, 0.15);
  border-color: #38bdf8;
  color: #38bdf8;
  font-weight: 600;
}}

.privacy-banner {{
  background: rgba(34, 197, 94, 0.1);
  border: 1px solid rgba(34, 197, 94, 0.25);
  border-radius: 8px;
  padding: 10px 12px;
  display: flex;
  gap: 10px;
  align-items: center;
  font-size: 11.5px;
  color: #4ade80;
  line-height: 1.4;
}}

/* Network & Traffic inspection */
.net-card {{
  background: #141926;
  border: 1px solid #242c3d;
  border-radius: 8px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}}
.net-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 11px;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  padding: 4px 6px;
  border-radius: 4px;
  background: #0f131f;
}}
.method-get {{ color: #60a5fa; font-weight: 700; }}
.method-post {{ color: #34d399; font-weight: 700; }}
.method-ws {{ color: #c084fc; font-weight: 700; }}
.status-200 {{ color: #4ade80; }}
.status-101 {{ color: #a78bfa; }}

/* Left web area: Developer inspection */
.dev-area {{
  flex: 1;
  background: #090d16;
  padding: 24px 30px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}}
.dev-headline {{
  font-size: 22px;
  font-weight: 800;
  color: #f8fafc;
}}
.dev-sub {{
  font-size: 13.5px;
  color: #94a3b8;
  line-height: 1.5;
  max-width: 620px;
}}
.code-preview {{
  background: #0f172a;
  border: 1px solid #1e293b;
  border-radius: 10px;
  padding: 18px;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 12.5px;
  color: #e2e8f0;
  line-height: 1.6;
  margin-top: 6px;
}}
</style>
</head>
<body>

  <!-- Top Header Banner -->
  <div class="store-header">
    <div class="header-title">
      {SVG_LOGO}
      <span>Cloakium Link</span>
      <span style="color:#64748b; font-weight:400; font-size:13px;">| Developer & AI Inspection</span>
    </div>
    <div class="header-badge">
      🛡️ Local-First Privacy & Multi-Provider AI
    </div>
    <div class="header-meta">
      <span>OpenAI</span>
      <span>•</span>
      <span>Claude</span>
      <span>•</span>
      <span>Gemini</span>
      <span>•</span>
      <span>DeepSeek</span>
      <span>•</span>
      <span>Ollama Local</span>
    </div>
  </div>

  <div class="browser-shell">
    <div class="chrome-tabbar">
      <div class="window-controls">
        <div class="win-dot close"></div>
        <div class="win-dot min"></div>
        <div class="win-dot max"></div>
      </div>
      <div class="chrome-tab">
        <span>⚙️ Developer Settings & Inspection</span>
      </div>
    </div>

    <div class="chrome-nav">
      <div class="nav-arrows">
        <span>←</span>
        <span>→</span>
        <span>↻</span>
      </div>
      <div class="url-bar">
        <span class="lock">🔒</span>
        <span class="host">chrome-extension://cloakium-link</span>
        <span>/settings</span>
      </div>
      <div class="ext-badge-active">
        {SVG_LOGO}
        <span>Settings View</span>
      </div>
    </div>

    <div class="workspace">
      <!-- Web content: Developer code preview -->
      <div class="dev-area">
        <div class="dev-headline">Inspect, Automate & Debug with Real Chrome Events</div>
        <div class="dev-sub">
          Cloakium Link uses Chrome DevTools Protocol (CDP) and webRequest to observe DOM events, network traffic, and console messages without altering the host web environment.
        </div>

        <div class="code-preview">
          <span style="color:#64748b;">// Chrome DevTools Protocol Hook</span><br>
          <span style="color:#38bdf8;">await</span> chrome.debugger.sendCommand({'{'} tabId {'}'}, <span style="color:#fde047;">"Network.enable"</span>);<br>
          <span style="color:#38bdf8;">await</span> chrome.debugger.sendCommand({'{'} tabId {'}'}, <span style="color:#fde047;">"Page.captureScreenshot"</span>, {'{'} format: <span style="color:#fde047;">"png"</span> {'}'});<br><br>
          <span style="color:#64748b;">// Local-First Security Promise</span><br>
          <span style="color:#34d399;">const</span> keys = <span style="color:#38bdf8;">await</span> chrome.storage.local.get(<span style="color:#fde047;">"apiKeys"</span>); <span style="color:#64748b;">// 100% Client-Side</span>
        </div>
      </div>

      <!-- Extension Side Panel -->
      <div class="side-panel">
        <div class="panel-appbar">
          <div class="brand-group">
            {SVG_LOGO}
            <span class="brand-name">Cloakium Link</span>
          </div>
          <div class="page-chip">
            <span class="dot-green"></span>
            <span>Local Vault Active</span>
          </div>
        </div>

        <div class="panel-tabbar">
          <div class="tab-btn">Chat</div>
          <div class="tab-btn">Remote</div>
          <div class="tab-btn">Network <span class="tab-badge">4</span></div>
          <div class="tab-btn active">Settings</div>
        </div>

        <div class="settings-view">
          <!-- Privacy Guarantee Banner -->
          <div class="privacy-banner">
            <div style="font-size:18px;">🔒</div>
            <div>
              <strong>100% Local Storage:</strong> All API keys, passwords, and sessions remain inside <code>chrome.storage.local</code>. Never uploaded to cloud.
            </div>
          </div>

          <!-- Active Provider Card -->
          <div class="provider-card">
            <div class="provider-header">
              <span class="provider-name">AI Model Provider</span>
              <span style="font-size:11px; color:#38bdf8; font-weight:600;">Claude 3.5 Sonnet</span>
            </div>
            <div class="provider-tags">
              <div class="ptag active">Anthropic Claude</div>
              <div class="ptag">OpenAI GPT-5</div>
              <div class="ptag">Google Gemini</div>
              <div class="ptag">DeepSeek</div>
              <div class="ptag">Ollama (127.0.0.1)</div>
            </div>
            <div style="background:#0f131f; border:1px solid #283147; border-radius:6px; padding:6px 10px; font-size:11.5px; font-family:monospace; color:#64748b;">
              sk-ant-api03-••••••••••••••••••••••••
            </div>
          </div>

          <!-- Real-time Network Traffic -->
          <div class="net-card">
            <div style="font-size:12px; font-weight:700; color:#cbd5e1; display:flex; justify-content:space-between;">
              <span>Live Traffic Stream</span>
              <span style="font-size:10px; color:#4ade80;">● Recording</span>
            </div>
            <div class="net-row">
              <span><span class="method-post">POST</span> /api/v1/agent/action</span>
              <span class="status-200">200 OK (28ms)</span>
            </div>
            <div class="net-row">
              <span><span class="method-get">GET</span> /api/v1/session/status</span>
              <span class="status-200">200 OK (14ms)</span>
            </div>
            <div class="net-row">
              <span><span class="method-ws">WS</span> wss://cloakium.site/ws</span>
              <span class="status-101">101 Switch (P2P)</span>
            </div>
          </div>

          <!-- CDP Status -->
          <div style="background:#161b2a; border:1px solid #283147; border-radius:8px; padding:10px 12px; font-size:11.5px; color:#94a3b8;">
            <div style="font-weight:700; color:#f8fafc; margin-bottom:4px;">CDP Integration Status</div>
            Debugger protocol active. Supports real mouse curves, touch simulation, and full-page layout captures.
          </div>
        </div>
      </div>
    </div>
  </div>

</body>
</html>'''
    render_html_to_png(html, "screenshot-3-developer-tools")

if __name__ == "__main__":
    print("Generating official Chrome Web Store screenshots (1280x800 and 640x400)...")
    generate_screenshot_1()
    generate_screenshot_2()
    generate_screenshot_3()
    print("All screenshots generated successfully in ./screenshots/")
