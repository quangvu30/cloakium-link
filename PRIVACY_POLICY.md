# Privacy Policy for Cloakium Link

Last updated: November 2026 (version 0.6.0)

Cloakium Link ("we", "our", or "the extension") is a Chrome extension that adds an AI assistant to your browser, saves and runs workflows, and lets you control your own Chrome remotely from Cloakium (https://cloakium.site), from a Telegram bot, or from a CLI agent.

This policy explains what data the extension handles, where it goes, and how you control it.

## 1. Our principles
- We do not sell your data, show ads, or track your browsing for profiling.
- The extension does not send your browsing history, page content, or keystrokes to Cloakium unless you use a feature that needs it (sections 3 and 4). You turn each of those features on yourself.
- Remote control and CLI agents are off by default.

## 2. Data stored only in your browser
The following stays in your Chrome profile (local extension storage) and is never sent to Cloakium:
- API keys for AI providers, and your model settings;
- your Telegram bot token and settings;
- the remote access password, kept only as a one-way hash, never in plain text;
- chat history, preferences and response overrides;
- network requests and console logs captured by the developer tools (Network, Log, Overrides). They are kept in memory for the open session and shown only to you. Sensitive header values such as cookies and authorization headers are hidden from the AI assistant, the Telegram bot and CLI agents.

You can delete this data at any time by clearing it in the extension or by removing the extension.

## 3. Data shared with Cloakium
These features only work when you sign in to Cloakium or pair the extension with your Cloakium account.

**Pairing (account link).** Cloakium stores the name you give this Chrome, a secure token that identifies it (only a hash of it is stored on our servers), when it was paired, and when and from which IP address it last connected. You can unpair a Chrome from the extension or remove it under **My Chrome** on Cloakium at any time.

**Workflow sync and Marketplace.** Workflows you save to your account, or add from the Marketplace, are stored on Cloakium so they can sync between your browsers. Workflows you publish to the Marketplace become visible to other users.

**Remote control.** When you connect from **My Chrome** on Cloakium, Cloakium relays only the messages that set up the connection. The screen picture and your mouse and keyboard input go directly between the two browsers. They do not pass through Cloakium servers, and we do not record them. Connection setup uses standard network servers (STUN) that can see the IP addresses of the two browsers.

**CLI agents (Claude Code, Codex, Gemini CLI and others).** If you turn on **Allow CLI agents** for a Chrome profile, an agent that holds your Cloakium API key can send it commands through Cloakium. In that case:
- the commands, and their results (for example page text, page details and screenshots), pass through Cloakium servers between your agent and your Chrome;
- Cloakium does not keep the commands' arguments or results after delivering them;
- for your account's security, Cloakium logs each command with the tool name, the Chrome it ran on, the API key used, whether it succeeded, the time and the IP address;
- what your agent does with the results, including sending them to its own AI provider, is governed by that agent's and that provider's terms.

**Other Cloakium services.** Some tools call Cloakium services on your behalf using this Chrome's pairing credential. The credential itself is never shared with web pages.

## 4. Third-party services
- **AI providers.** When you use the AI assistant with your own API key, your messages and the page content needed for the task are sent directly from your browser to the provider you chose (for example Anthropic, OpenAI, or a compatible service), not through Cloakium. Their privacy policies apply. If you choose the on-device model, nothing leaves your computer.
- **Telegram.** If you set up a Telegram bot, the messages, replies and screenshots you exchange with it go through Telegram. Telegram's privacy policy applies.

## 5. Chrome permissions
Cloakium Link asks only for the permissions its features need:
- `debugger`: takes screenshots, sends real mouse and keyboard input, and powers the developer tools and response overrides. Chrome shows a yellow notice bar while it is in use.
- `webRequest`: shows network requests in the Network tool.
- `host_permissions` (`<all_urls>`) and `scripting`: let the assistant read and act on the pages you ask it to work on.
- `tabs` and `activeTab`: find, open and switch between tabs.
- `sidePanel`: shows the extension beside the page.
- `offscreen`: keeps the connection for remote control and CLI agents running in the background.
- `storage`: saves your settings and history in your browser.
- `notifications`: tells you when a remote session, the Telegram bot or a CLI agent starts controlling this Chrome, when a remote session ends, when someone enters a wrong access password, and when this Chrome is unpaired.
- `downloads`: saves files, exports and screenshots you ask for.

## 6. Your control
- Remote control and CLI agents are off until you turn them on, and you can turn them off at any time.
- While Chrome is being controlled, the extension icon shows **LIVE** or **CLI**, you get a notification, and a **Disconnect** button in the side panel stops it at once.
- You can revoke Cloakium API keys on the **API keys** page, and unpair or remove a Chrome under **My Chrome**.

## 7. Children's privacy
Cloakium Link is not intended for children under 13 and does not knowingly collect personal information from them.

## 8. Changes to this policy
We may update this policy when the extension changes. Updates are published on this page with a new date.

## 9. Contact
For questions about this policy, contact us through https://cloakium.site.
