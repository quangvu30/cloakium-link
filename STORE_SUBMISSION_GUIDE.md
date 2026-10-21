# Hướng Dẫn Chi Tiết Publish Cloakium Link Lên Chrome Web Store

Tài liệu này chuẩn bị sẵn toàn bộ thông tin, nội dung mô tả, và **văn bản giải trình quyền (Permission Justifications)** cần thiết khi gửi duyệt trên **Chrome Web Store Developer Dashboard**.

---

## 1. Chuẩn bị tài khoản & file cài đặt

### 1.1. Tài khoản Chrome Web Store Developer
1. Truy cập [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole/).
2. Đăng nhập bằng tài khoản Google bạn muốn quản lý extension.
3. Bật **Xác thực 2 bước (2-Step Verification)** cho tài khoản Google (bắt buộc).
4. Thanh toán phí kích hoạt tài khoản Developer: **$5 USD** (chỉ trả 1 lần duy nhất).

### 1.2. File nén tải lên (Package ZIP)
> [!IMPORTANT]
> Chrome Web Store yêu cầu file `manifest.json` phải nằm ngay thư mục gốc của file ZIP (không được bọc trong một thư mục con).

- Dự án đã tạo sẵn script `pack.sh`. Mỗi khi muốn đóng gói bản mới, chỉ cần chạy:
  ```bash
  ./pack.sh
  ```
- File zip chuẩn được tạo ra tại: `cloakium-link-store.zip` (ở thư mục gốc của repo).
- Dùng file `cloakium-link-store.zip` này để upload lên Developer Console (bấm **Add new item** hoặc **Upload new package**).

---

## 2. Store Listing (Thông tin hiển thị trên cửa hàng)

### 2.1. Basic Information
- **Item Name**: `Cloakium Link` (hoặc hệ thống tự nhận diện từ `manifest.json` qua `_locales`)
- **Summary / Short Description**:
  > Control your own Chrome from Cloakium, give tasks to an AI agent with your own API key, and command it through a Telegram bot.
- **Detailed Description (Mô tả chi tiết)**:
  *(Copy đoạn bên dưới dán vào ô Description)*

```markdown
Cloakium Link connects your Chrome browser directly to Cloakium (https://cloakium.site), turning your browser into a secure, remotely manageable workspace with built-in AI agent capabilities.

KEY FEATURES:
- Remote Browser Access: View and interact with your browser sessions directly from the Cloakium web platform via secure, peer-to-peer WebRTC connections.
- AI Automation Agent: Assign browsing and inspection tasks to AI agents using your own LLM API keys (OpenAI, Claude, Gemini, DeepSeek, or local Ollama).
- Telegram Bot Integration: Trigger actions, query browser status, or receive task completion alerts right inside your Telegram chat.
- Developer Inspection & Debugging: Inspect network requests, monitor console logs, and take automated full-page screenshots.
- Privacy & Local-First Security: All API keys, bot tokens, and access passwords remain stored locally inside your browser (chrome.storage.local) and are never sent to external servers. Password authentication uses Argon2id hashing.

HOW TO USE:
1. Open the Cloakium Link side panel (or press Alt+Shift+A).
2. Go to the "Remote" tab, paste the pairing code from Cloakium (tab "My Chrome"), set an access password, and enable remote control.
3. Add your LLM API keys in the Settings tab if you wish to run AI automations.
```

- **Category**: `Developer Tools` hoặc `Productivity`.
- **Primary Language**: `English` (Extension đã hỗ trợ cả tiếng Anh và tiếng Việt qua `_locales`).

### 2.2. Graphic Assets (Hình ảnh)
- **Store Icon**: Dùng file `cloakium-link/icons/icon128.png` (kích thước chuẩn 128x128 PNG).
- **Screenshots (Bắt buộc tối thiểu 1 ảnh)**:
  - Kích thước hợp lệ: **1280x800** px hoặc **640x400** px (JPEG hoặc 24-bit PNG không có alpha/transparency).
  - *Gợi ý*: Chụp 2-3 màn hình thực tế:
    1. Giao diện Side panel của Cloakium Link (tab Remote / Ghép nối).
    2. Giao diện Agent AI / Chat.
    3. Màn hình điều khiển trình duyệt từ web Cloakium.
- **Small Promo Tile (Tùy chọn)**: Kích thước 440x280 px (nếu muốn được hiển thị nổi bật).

---

## 3. Privacy Practices (Khai báo quyền riêng tư & Giải trình quyền)

> [!WARNING]
> Do extension sử dụng các quyền cao cấp như `debugger`, `webRequest`, và `<all_urls>`, nhân viên xét duyệt Google (Human Reviewer) sẽ kiểm tra rất kỹ. Bắt buộc phải điền đầy đủ và chính xác các mục sau.

### 3.1. Single Purpose (Mục đích duy nhất của extension)
*(Dán vào ô Single Purpose Description)*
```text
Cloakium Link provides a developer automation and remote browser companion that enables users to control their own Chrome session from Cloakium, inspect network/console traffic, and automate web tasks with AI using local credentials.
```

### 3.2. Permission Justifications (Giải trình lý do cần từng quyền)
Khi bảng điều khiển hỏi lý do cấp phép cho từng permission, dán nội dung tương ứng dưới đây:

- **debugger**:
  ```text
  Required to attach the Chrome DevTools Protocol (CDP) to user-selected tabs in order to capture high-resolution screenshots, simulate trusted keyboard and mouse inputs for browser automation, and inspect network traffic.
  ```

- **webRequest**:
  ```text
  Required to monitor HTTP/HTTPS requests on open pages so developers and the AI agent can inspect API calls, debug network latency, and capture request/response metadata in real-time.
  ```

- **Host Permissions (`<all_urls>`)**:
  ```text
  The extension functions as a general browser automation and developer debugging assistant. It must be able to interact with and inspect any website that the user chooses to navigate to, automate, or debug.
  ```

- **storage**:
  ```text
  Used to persist user settings, local chat history, session state, and user-provided LLM API keys securely on the user's local machine (chrome.storage.local).
  ```

- **activeTab & tabs**:
  ```text
  Required to list and navigate between open tabs, query the current page status, and allow the user to select which specific tab should be inspected or controlled remotely.
  ```

- **scripting**:
  ```text
  Required to inject light content scripts and bridge listeners into web pages to capture DOM events, console logs, and errors for the side panel interface.
  ```

- **sidePanel**:
  ```text
  Used to present the extension's primary interface (AI chat, session controls, and settings) directly alongside the user's active browsing tab without blocking the page content.
  ```

- **offscreen**:
  ```text
  Required to maintain WebRTC peer-to-peer data channels and handle media capture/streaming tasks in an isolated offscreen document without blocking the background service worker.
  ```

- **notifications**:
  ```text
  Required to notify the user whenever a remote session connects, disconnects, or completes an automated background task, ensuring complete transparency and security.
  ```

- **downloads**:
  ```text
  Allows users to export task logs, debugging traces, and captured screenshots directly to their local download folder.
  ```

### 3.3. Data Usage (Khai báo sử dụng dữ liệu)
Trong phần **Data usage**:
- Đánh dấu xác nhận cam kết:
  - *"I certify that my extension adheres to the Chrome Web Store Developer Program Policies."*
  - *"I confirm that my extension does not sell user data to third parties."*
  - *"I confirm that my extension does not use or transfer user data for purposes unrelated to the item's single purpose."*
  - *"I confirm that my extension does not use or transfer user data to determine creditworthiness or for lending purposes."*
- Nếu có câu hỏi về các loại dữ liệu thu thập (Personal information, Authentication information...):
  - Khai báo: Extension **chỉ lưu trữ trên máy cá nhân (`chrome.storage.local`)**, không truyền tải thông tin này về máy chủ của nhà phát triển.
  - Điền giải thích:
    ```text
    All credentials, bot tokens, and LLM API keys are stored solely on the client machine via chrome.storage.local. No user data, keystrokes, or personal credentials are collected, logged, or transferred to any developer-owned or third-party servers.
    ```

---

## 4. Privacy Policy (Chính sách bảo mật)

Google bắt buộc cung cấp một đường dẫn **Privacy Policy URL** hợp lệ và công khai khi extension yêu cầu quyền `<all_urls>` hoặc `debugger`.

Bạn có thể tạo một trang tại: `https://cloakium.site/privacy` hoặc tạo một file markdown trên GitHub Pages / Gist.

Nội dung mẫu Privacy Policy được cung cấp tại: [PRIVACY_POLICY.md](PRIVACY_POLICY.md).

---

## 5. Quy trình gửi duyệt & thời gian chờ

1. Bấm **Submit for Review** (Gửi để xét duyệt).
2. Khi có hộp thoại hỏi về việc xuất bản:
   - Có thể chọn **Publish automatically** (Tự động công khai sau khi duyệt xong) hoặc **Publish manually** (Bạn tự bấm Publish sau khi Google phê duyệt).
3. **Thời gian duyệt**:
   - Đối với các extension thông thường: 1 - 3 ngày.
   - Đối với extension có quyền `debugger` + `<all_urls>`: Thường mất **3 - 7 ngày làm việc** vì Google đưa vào luồng kiểm duyệt thủ công (Manual Review).
4. **Nếu Google gửi email yêu cầu làm rõ (Clarification / Justification Request)**:
   - Google có thể gửi email hỏi kỹ hơn về việc tại sao cần `debugger` hoặc yêu cầu một video demo ngắn (quay màn hình cách dùng, upload lên YouTube chế độ Unlisted). Nếu nhận được email này, chỉ cần cung cấp link video demo và trích dẫn lại mục đích hỗ trợ automation & developer debugging như ở mục 3.2.
