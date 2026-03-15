# PRD (Tài Liệu Yêu Cầu Sản Phẩm)

## Phạm vi sản phẩm

GrowthSO MVP là nền tảng web + mobile cho vận hành SEO và tăng trưởng số có AI hỗ trợ.

## Bài toán

Đội ngũ không thể tối ưu nhanh và nhất quán SEO, ads, content, review khi đang dùng nhiều công cụ rời rạc.

## Phạm vi chức năng MVP

1. Onboard domain và hồ sơ doanh nghiệp
2. Crawl SEO, phát hiện issue, theo dõi thứ hạng
3. AI tạo brief và draft nội dung
4. Ingestion review, sentiment, gợi ý phản hồi
5. Ingestion hiệu suất ads, gợi ý tối ưu ngân sách
6. Dashboard KPI hợp nhất và action queue
7. Phân quyền theo tổ chức/workspace

## Mục tiêu kỹ thuật

- Availability API: `99.9%`
- P95 API read: `< 400ms`
- Isolation dữ liệu theo tenant
- SLA cập nhật dashboard hàng ngày
- Audit log cho hành động quan trọng

## Mục tiêu scale

- Lộ trình kiến trúc hướng tới `1M users`
- Event-driven pipeline cho workload bất đồng bộ
- Horizontal scaling cho API và worker
