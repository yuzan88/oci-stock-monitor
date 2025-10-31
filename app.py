import streamlit as st
import requests
from bs4 import BeautifulSoup

# Telegram 配置（从 secrets.toml 读取）
TELEGRAM_TOKEN = st.secrets["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = st.secrets["TELEGRAM_CHAT_ID"]

URL = "https://oci.ee/cart?fid=5"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        r = requests.post(url, json=payload)
        r.raise_for_status()
        st.success("📨 Telegram 已发送")
    except Exception as e:
        st.error(f"Telegram 发送失败：{e}")

def check_stock():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        stock_info = soup.find(text=lambda t: "库存：" in t)
        if stock_info:
            stock_count = int(stock_info.split("库存：")[1].split()[0])
            if stock_count > 0:
                message = f"✅ OCI 有库存啦！数量：{stock_count}\n{URL}"
                send_telegram_message(message)
                return f"✅ 有库存：{stock_count}"
            else:
                return "❌ 暂无库存"
        else:
            return "⚠️ 未找到库存信息"
    except Exception as e:
        return f"请求失败：{e}"

st.title("OCI VPS 库存监控")
if st.button("立即检查库存"):
    result = check_stock()
    st.write(result)
if st.button("测试 Telegram 通知"):
    send_telegram_message("✅ Telegram 测试成功！")

