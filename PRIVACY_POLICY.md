# Privacy Policy for Cloakium Link

Last updated: October 2026

Cloakium Link ("we", "our", or "the extension") is a Chrome browser extension designed to help users remotely monitor and interact with their own browser sessions from Cloakium (https://cloakium.site) and automate tasks using AI agents.

We respect your privacy and are committed to protecting it. This Privacy Policy outlines our data handling practices.

## 1. Data Collection and Transmission
- **No Data Collection to Remote Servers**: Cloakium Link does NOT collect, harvest, track, or sell your personal data, browsing history, keystrokes, or search queries.
- **Local Storage Only**: All user configurations, including LLM API keys (OpenAI, Claude, Gemini, DeepSeek, etc.), Telegram bot tokens, session logs, and access passwords, are saved solely in your local browser storage (`chrome.storage.local`).
- **Encrypted & Hashed Secrets**: Access passwords are never stored in plaintext; they are hashed locally using Argon2id.
- **Peer-to-Peer Transmission**: Media and remote control inputs are transmitted directly peer-to-peer between your browser and your remote client using encrypted WebRTC connections. The Cloakium signaling server is only used to relay initial connection handshakes and does not intercept session payloads.

## 2. Chrome Permissions Usage
Cloakium Link requests specific permissions to perform its core functions:
- `debugger`: Used to attach Chrome DevTools Protocol (CDP) for taking viewport/full-page screenshots and simulating trusted mouse and keyboard events during automated workflows. A yellow banner is shown by Chrome whenever this is active.
- `webRequest`: Used solely to capture network request/response headers on active tabs so that the user and local AI agent can debug API interactions.
- `host_permissions (<all_urls>)`: Enables the extension to automate tasks and inspect content on any web page selected by the user.
- `tabs` & `activeTab`: Used to identify open tabs, navigate between them, and control the active tab during remote or automated sessions.
- `sidePanel`: Used to display the user interface, session history, and control settings beside the browsing window.
- `offscreen`: Used to maintain background WebRTC communication channels and process offscreen tasks smoothly.
- `storage`: Used to save preferences, local chat history, and API configurations on your machine.
- `notifications`: Alerts you when a remote session connects, disconnects, or completes an automation task.
- `downloads`: Allows you to export debug logs, reports, or captured screenshots directly to your device.

## 3. Third-Party Services
When you use AI agent automation features, requests are sent directly from your browser to the AI service provider you have configured (e.g., Anthropic, OpenAI, Google, DeepSeek) using your personal API key. Your data is subject to the respective privacy policies of those providers.

## 4. Children's Privacy
Cloakium Link does not knowingly collect or solicit any personal information from children under the age of 13.

## 5. Changes to This Policy
We may update this Privacy Policy from time to time. Any changes will be posted on this page with an updated revision date.

## 6. Contact Us
If you have any questions or concerns regarding this Privacy Policy, please contact us via GitHub or at https://cloakium.site.
