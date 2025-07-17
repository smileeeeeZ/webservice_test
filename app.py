from flask import Flask, request
import hashlib
import xml.etree.ElementTree as ET
import base64
import os

app = Flask(__name__)

# 你设置的Token和EncodingAESKey
TOKEN = "4JbeDfxug76qn2CYzxG6BFa"
EncodingAESKey = "AX1FNdefWyCmjyoxlfAfVgCxCBXEPJUb6XsRBUovLMB"


@app.route("/", methods=["GET", "POST"])
def wechat():
    if request.method == "GET":
        # 验证URL是否有效
        signature = request.args.get("msg_signature")
        timestamp = request.args.get("timestamp")
        nonce = request.args.get("nonce")
        echostr = request.args.get("echostr")

        # 用 Token + timestamp + nonce 进行排序后 sha1 加密，与 signature 比较
        check_list = [TOKEN, timestamp, nonce]
        check_list.sort()
        s = ''.join(check_list)
        hashcode = hashlib.sha1(s.encode('utf-8')).hexdigest()

        # 如果签名一致，返回 echostr 给企业微信
        if hashcode == signature:
            return echostr
        else:
            return "signature error", 403

    return "OK"


if __name__ == '__main__':
    app.run(debug=True)
