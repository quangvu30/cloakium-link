# Cloakium Link

**Trợ lý AI, tự động hoá và điều khiển từ xa cho chính trình duyệt Chrome của bạn.**

Cloakium Link biến Chrome thành một trợ lý làm việc thực thụ: hiểu trang bạn đang xem, tự thao tác thay bạn, lưu lại quy trình để chạy lại, và cho phép bạn điều khiển Chrome từ xa qua [Cloakium](https://cloakium.site), Telegram hoặc agent CLI.

[English below](#cloakium-link-english)

## Tính năng

### Trợ lý AI ngay cạnh trang web
- Trò chuyện trong side panel về trang đang mở: tóm tắt, dịch, giải thích đoạn văn bản, tìm thông tin.
- Giao việc bằng ngôn ngữ tự nhiên: trợ lý tự bấm, nhập liệu, chuyển trang, mở tab, chụp màn hình, tải file lên và tải file về.
- Dùng API key của riêng bạn với Anthropic, OpenAI hoặc dịch vụ tương thích, hoặc chọn mô hình chạy ngay trên máy, không cần key.
- Các thao tác quan trọng luôn chờ bạn đồng ý trước khi thực hiện.

### Workflow: làm một lần, chạy mãi
- Lưu chuỗi thao tác vừa làm thành workflow, chạy lại chỉ với một lệnh, có thể truyền tham số.
- Đồng bộ workflow với tài khoản Cloakium để dùng trên nhiều Chrome.
- Thêm workflow có sẵn từ Marketplace của cộng đồng.
- Mỗi workflow xin quyền một lần trước lần chạy đầu tiên.

### Điều khiển Chrome từ xa
- Xem và điều khiển Chrome của bạn từ mục **Chrome của tôi** trên Cloakium, ở bất cứ đâu.
- Mỗi lần kết nối cần mật khẩu truy cập do bạn đặt.
- Quản lý nhiều Chrome trên một tài khoản (theo gói Cloakium Link).

### Bot Telegram của riêng bạn
- Giao việc cho trợ lý, xem ảnh chụp màn hình, chuyển tab, mở địa chỉ và chạy workflow ngay từ điện thoại.

### Kết nối agent CLI
- Cho Claude Code, Codex, Gemini CLI và các agent khác dùng Chrome của bạn để làm việc trên web.
- Không cần cài thêm gì trên máy: chỉ cần API key Cloakium và bộ skill có sẵn trên trang **API key**.
- Bật riêng cho từng profile Chrome, yêu cầu gói Cloakium Link.

### Công cụ cho lập trình viên
- **Network**: theo dõi request, xem header, payload, response và message WebSocket, sao chép dưới dạng cURL.
- **Log**: xem console của trang theo cùng một giao diện.
- **Overrides**: thay nội dung phản hồi của trang để thử nghiệm, tương tự Local Overrides của DevTools.

## Cài đặt

1. Tải [`cloakium-link.zip`](cloakium-link.zip) (nút **Download raw file**) rồi giải nén. Hoặc `git clone` repo này và dùng thư mục `cloakium-link/`.
2. Mở `chrome://extensions`, bật **Developer mode** ở góc trên bên phải.
3. Bấm **Load unpacked** và chọn thư mục vừa giải nén (thư mục có file `manifest.json`).
4. Bấm biểu tượng Cloakium Link để mở side panel.
   - Dùng trợ lý AI: vào **Cài đặt**, chọn mô hình và nhập API key.
   - Điều khiển từ xa: vào tab **Từ xa**, dán mã ghép lấy ở Cloakium → **Chrome của tôi**, đặt mật khẩu truy cập rồi bật **Cho phép điều khiển từ xa**.

**Cập nhật:** tải bản zip mới, giải nén đè lên thư mục cũ (hoặc `git pull`), rồi bấm **Reload** ở Cloakium Link trong `chrome://extensions`. Cấu hình đã lưu được giữ nguyên.

Yêu cầu Chrome 116 trở lên. Mô hình chạy trên máy cần Chrome 138 trở lên trên máy tính.

## Bạn luôn nắm quyền kiểm soát

- Điều khiển từ xa và agent CLI đều **tắt theo mặc định**, chỉ hoạt động khi bạn tự bật.
- Khi Chrome đang được điều khiển, biểu tượng extension hiện nhãn **LIVE** hoặc **CLI**, kèm thông báo và nút **Ngắt** để dừng ngay lập tức.
- API key, token bot Telegram và mật khẩu truy cập chỉ lưu trong Chrome của bạn, không gửi lên Cloakium.
- Hình ảnh khi điều khiển từ xa đi thẳng giữa hai trình duyệt, không đi qua máy chủ.
- Chrome hiện thanh thông báo màu vàng mỗi khi extension trực tiếp thao tác trên trang.

Extension cần quyền đọc và thao tác trên các trang web, quản lý tab, gửi thông báo và tải file để thực hiện các tính năng trên. Chi tiết xem tại [Chính sách bảo mật](PRIVACY_POLICY.md).

## Về repo này

Repo chỉ chứa **bản build** để cài đặt. Mỗi lần phát hành, `cloakium-link.zip` và thư mục `cloakium-link/` được thay bằng bản mới nhất; số phiên bản ghi trong `cloakium-link/manifest.json` và lịch sử commit.

Hỗ trợ và gói dịch vụ: [cloakium.site](https://cloakium.site)

---

# Cloakium Link (English)

**An AI assistant, automation and remote control for your own Chrome.**

Cloakium Link turns Chrome into a real working assistant: it understands the page you are on, acts for you, saves your routines to run again, and lets you control Chrome remotely through [Cloakium](https://cloakium.site), Telegram or a CLI agent.

## Features

### An AI assistant beside every page
- Chat in the side panel about the open page: summarize, translate, explain a passage, find information.
- Give tasks in plain language: the assistant clicks, types, navigates, opens tabs, takes screenshots, uploads and downloads files.
- Bring your own API key for Anthropic, OpenAI or a compatible service, or pick an on-device model that needs no key.
- Important actions always wait for your approval first.

### Workflows: do it once, run it any time
- Save what you just did as a workflow and run it again with one command, with parameters.
- Sync workflows with your Cloakium account to use them on several Chrome browsers.
- Add ready-made workflows from the community Marketplace.
- Each workflow asks for its permissions once, before its first run.

### Remote control
- See and control your Chrome from **My Chrome** on Cloakium, from anywhere.
- Every connection requires an access password you set.
- Manage several Chrome browsers on one account (depending on your Cloakium Link plan).

### Your own Telegram bot
- Give the assistant tasks, get screenshots, switch tabs, open addresses and run workflows from your phone.

### CLI agents
- Let Claude Code, Codex, Gemini CLI and other agents use your Chrome to work on the web.
- Nothing to install locally: just a Cloakium API key and the ready-made skill on the **API keys** page.
- Turned on per Chrome profile; requires a Cloakium Link plan.

### Developer tools
- **Network**: follow requests, inspect headers, payloads, responses and WebSocket messages, copy as cURL.
- **Log**: the page's console in the same layout.
- **Overrides**: replace a page's responses for testing, like DevTools Local Overrides.

## Install

1. Download [`cloakium-link.zip`](cloakium-link.zip) (**Download raw file**) and unzip it, or `git clone` this repository and use the `cloakium-link/` folder.
2. Open `chrome://extensions` and turn on **Developer mode** (top right).
3. Click **Load unpacked** and pick the unzipped folder (the one containing `manifest.json`).
4. Click the Cloakium Link icon to open the side panel.
   - AI assistant: open **Settings**, choose a model and enter your API key.
   - Remote control: in the **Remote** tab, paste the pairing code from Cloakium → **My Chrome**, set an access password and turn on **Allow remote control**.

**Update:** download the new zip, unzip it over the old folder (or `git pull`), then click **Reload** on Cloakium Link in `chrome://extensions`. Saved settings are kept.

Requires Chrome 116 or later. The on-device model needs desktop Chrome 138 or later.

## You stay in control

- Remote control and CLI agents are **off by default** and only work once you turn them on.
- While Chrome is being controlled, the extension icon shows **LIVE** or **CLI**, with a notification and a **Disconnect** button that stops it at once.
- API keys, the Telegram bot token and the access password stay in your Chrome and are never sent to Cloakium.
- The remote picture goes straight between the two browsers, not through a server.
- Chrome shows its yellow notice bar whenever the extension acts directly on a page.

The extension needs access to read and act on web pages, manage tabs, show notifications and download files to provide these features. See the [Privacy Policy](PRIVACY_POLICY.md) for details.

## About this repository

This repository holds the **build** only. Each release replaces `cloakium-link.zip` and the `cloakium-link/` folder; the version is in `cloakium-link/manifest.json` and in the commit history.

Support and plans: [cloakium.site](https://cloakium.site)
