from sanic import Sanic
from sanic.response import text

from sanic_fcm import SanicFCM, FCMMessage


FCM_API_KEY = '<FCM_API_KEY>'
registration_id = '<registration_id>'

app = Sanic()
app.config['FCM_API_KEY'] = FCM_API_KEY
sanic_fcm = SanicFCM(app)


@app.route("/uber")
async def hello(request):
    msg = FCMMessage(registration_id,
                     message_title="Uber update",
                     message_body="Hi john, your customized news for today is ready")
    await sanic_fcm.fcm.send(msg)
    return text("sent")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
