from flask import Flask,request,abort

from linebot import(
    LineBotApi,WebhookHandler
)

from linebot.exceptions import(
    InvalidSignatureError
) 
from linebot.models import(
    MessageEvent,TextMessage,TextSendMessage
)
import os

+body
app = Flask(__name__)

Access_token = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
Sercret = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(Access_token)
handler = WebhookHandler(Sercret)

@app.route("/callback",methods = ["POST"])
def callback();
    signature = request.headers["X-Line-Signature"]

    body = request.get_data(as_text=True)
    app.logger.info("Request body:")

    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

@handler.add(MessageEvent,message = TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=event.message.text)
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT",5000))
    app.run(host="0.0.0.0",port = port)
