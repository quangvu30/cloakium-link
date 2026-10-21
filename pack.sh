#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_ZIP="$DIR/cloakium-link-store.zip"

echo "Đang đóng gói extension cho Chrome Web Store..."

# Xóa zip cũ nếu có
rm -f "$OUTPUT_ZIP"

# Đóng gói trực tiếp nội dung trong thư mục cloakium-link/
cd "$DIR/cloakium-link"
zip -q -r "$OUTPUT_ZIP" . -x ".*" -x "__MACOSX/*" -x "*.DS_Store"

echo "Đã tạo thành công: $OUTPUT_ZIP"
echo "Kiểm tra cấu trúc zip:"
unzip -l "$OUTPUT_ZIP" | head -n 15
