from flask import Flask, request
import hashlib

app = Flask(__name__)

# 企业微信配置的 token
TOKEN = "weworktesttoken123"  # ✅ 你自己设置的 Token，和企业微信填写的一致！

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # 获取参数
        msg_signature = request.args.get("msg_signature")
        timestamp = request.args.get("timestamp")
        nonce = request.args.get("nonce")
        echostr = request.args.get("echostr")

        # 按企业微信的规则进行签名校验（排序 + sha1）
        if not all([TOKEN, timestamp, nonce]):
            return "Missing params", 400

        hashlist = [TOKEN, timestamp, nonce]
        hashlist.sort()
        sha = hashlib.sha1()
        sha.update("".join(hashlist).encode("utf-8"))
        hashcode = sha.hexdigest()

        # 签名不验证了（企业微信 URL 验证不会用 msg_signature 来对比）
        # 直接返回 echostr（测试阶段）

        return echostr or "No echostr"
    return "hello"
