# Cloakium Link

Extension Chrome để xem và điều khiển Chrome của chính bạn từ [Cloakium](https://cloakium.site) (tab **Chrome của tôi**), giao việc cho agent AI bằng API key của bạn, và ra lệnh qua bot Telegram của bạn.

Repo này chỉ chứa **bản build** để cài. Mỗi lần phát hành, `cloakium-link.zip` và thư mục `cloakium-link/` được thay bằng bản mới nhất; phiên bản ghi trong `cloakium-link/manifest.json` và trong lịch sử commit.

## Cài đặt

1. Tải [`cloakium-link.zip`](cloakium-link.zip) (nút **Download raw file**) rồi giải nén. Hoặc `git clone` repo này và dùng thư mục `cloakium-link/`.
2. Mở `chrome://extensions`, bật **Developer mode** (góc trên bên phải).
3. Bấm **Load unpacked** và chọn thư mục vừa giải nén (thư mục có `manifest.json`).
4. Bấm biểu tượng Cloakium Link để mở side panel, vào tab **Từ xa**:
   - dán mã ghép tạo ở Cloakium → **Chrome của tôi**,
   - đặt mật khẩu truy cập,
   - bật **Cho phép điều khiển từ xa**.

Cập nhật: tải zip mới, giải nén đè lên thư mục cũ (hoặc `git pull`), rồi bấm **Reload** ở Cloakium Link trong `chrome://extensions`. Cấu hình đã lưu được giữ nguyên.

## Quyền và dữ liệu

- Cần quyền `debugger` (điều khiển bằng sự kiện chuột/phím thật, Chrome hiện thanh vàng "đang gỡ lỗi" khi đang dùng), `tabs`, `offscreen`, `notifications` và quyền truy cập mọi trang (cho agent đọc và thao tác trang).
- API key LLM, bot token Telegram và mật khẩu truy cập chỉ lưu trong Chrome của bạn (`chrome.storage.local`), không gửi lên Cloakium. Mật khẩu lưu dạng băm Argon2id.
- Hình ảnh và thao tác đi thẳng giữa hai trình duyệt (WebRTC); Cloakium chỉ chuyển tin nhắn bắt tay.
- Khi đang bị điều khiển: biểu tượng extension hiện **LIVE** màu đỏ, có thông báo hệ thống và nút **Ngắt** trong side panel.
- Xem chi tiết tại [Chính sách bảo mật (Privacy Policy)](PRIVACY_POLICY.md).

---

# Cloakium Link (English)

A Chrome extension to see and control your own Chrome from [Cloakium](https://cloakium.site) (the **My Chrome** tab), give tasks to an AI agent with your own API key, and command it through your own Telegram bot.

This repository holds the **build** only. Each release replaces `cloakium-link.zip` and the `cloakium-link/` folder; the version is in `cloakium-link/manifest.json` and in the commit history.

## Install

1. Download [`cloakium-link.zip`](cloakium-link.zip) (**Download raw file**) and unzip it, or `git clone` this repository and use the `cloakium-link/` folder.
2. Open `chrome://extensions` and turn on **Developer mode** (top right).
3. Click **Load unpacked** and pick the unzipped folder (the one with `manifest.json`).
4. Click the Cloakium Link icon to open the side panel, then in the **Remote** tab:
   - paste the pairing code from Cloakium → **My Chrome**,
   - set an access password,
   - turn on **Allow remote control**.

Update: download the new zip, unzip it over the old folder (or `git pull`), then click **Reload** on Cloakium Link in `chrome://extensions`. Saved settings are kept.

## Permissions and data

- Needs `debugger` (real mouse and keyboard events; Chrome shows its yellow "debugging" bar while in use), `tabs`, `offscreen`, `notifications` and access to all sites (so the agent can read and act on pages).
- LLM API keys, the Telegram bot token and the access password stay in your Chrome (`chrome.storage.local`) and are never sent to Cloakium. The password is stored as an Argon2id hash.
- Picture and input go straight between the two browsers (WebRTC); Cloakium only relays the handshake.
- While it is being controlled: a red **LIVE** badge on the extension icon, a system notification and a **Disconnect** button in the side panel.
- Read our full [Privacy Policy](PRIVACY_POLICY.md).
