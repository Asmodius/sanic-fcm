import pprint
import asyncio

from sanic_fcm import FCMMessage, FCM

loop = asyncio.get_event_loop()


async def send_fcm():
    apy_key = ('AAAAX9g1pF4:APA91bGiOWHhq7vCuPjzm-V79CMp7pnbASTaYN7pWf1lPH7P8DCWtL9_OYCmQKY'
               '-qb2DmIdjdxbk3NyDPJpWVrzMJzXnLYqUJzmM1UH3O2e89DNGguhSOBlrC4DWkC8uSzCDO0M2mvB6')
    registration_id = (
        '9WNAyu45m-RHB9VA9aT2XzQnePEgbegFHxdlbuFXB7MELt_JFVm7faFYUIrPYoHcXsRmDoMrBV4SHA'
        '0Kjm-y215vf_Uz1-1j6e933hbYXtVEsX6gMwyU0_eWSy2KrSpYfxVwLZoN_VdrYi9cYb/retMs')

    msg = FCMMessage([registration_id],
                     message_title="Uber update",
                     message_body="Hi john, your customized news for today is ready",
                     priority=False,
                     dry_run=True)
    pprint.pprint(msg.payload)

    fcm = FCM(apy_key)
    x = await fcm.send(msg)
    print('x', x)
    # err = {'multicast_id': -1, 'success': 0, 'failure': 1, 'canonical_ids': 0, 'results': [{'error': 'InvalidRegistration'}]}

if __name__ == '__main__':
    loop.run_until_complete(send_fcm())
