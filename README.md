\# OCI VPS 库存监控器



这是一个使用 Streamlit 构建的网页应用，用于监控 \[OCI](https://oci.ee) VPS 的库存情况，并通过 Telegram 发送提醒。



\## 功能



\- 实时检查库存

\- 一键发送 Telegram 通知

\- 部署在 Streamlit Cloud，无需本地运行



\## 使用方法



1\. 点击按钮检查库存

2\. 如果有货，将自动发送 Telegram 消息



\## 部署方法



1\. Fork 或 Clone 本项目到你的 GitHub

2\. 登录 \[Streamlit Cloud](https://share.streamlit.io)

3\. 创建新应用，选择你的仓库和 `app.py`

4\. 在 Secrets 页面添加以下内容：



```toml

TELEGRAM\_TOKEN = "你的BotToken"

TELEGRAM\_CHAT\_ID = "你的用户ID"



