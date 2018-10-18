from pyfcm import FCMNotification

# FCM_API_KEY = 'AIzaSyCjBdZMAfObGEQ-JW44lZEcrZ6cQp5pPy0'  # заменить на боевом сервере!
# заменить на боевом сервере!
FCM_API_KEY = ('AAAAX9g1pF4:APA91bGiOWHhq7vCuPjzm-V79CMp7pnbASTaYN7pWf1lPH7P8DCWtL9_OYCmQKY'
               '-qb2DmIdjdxbk3NyDPJpWVrzMJzXnLYqUJzmM1UH3O2e89DNGguhSOBlrC4DWkC8uSzCDO0M2mvB6')

push_service = FCMNotification(api_key=FCM_API_KEY)

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

# registration_id = '0:1432811719975865%54f79db3f9fd7ecd'
registration_id = ('9WNAyu45m-RHB9VA9aT2XzQnePEgbegFHxdlbuFXB7MELt_JFVm7faFYUIrPYoHcXsRmDoMrBV4SHA'
                   '0Kjm-y215vf_Uz1-1j6e933hbYXtVEsX6gMwyU0_eWSy2KrSpYfxVwLZoN_VdrYi9cYb/retMs')

message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id,
                                           message_title=message_title,
                                           message_body=message_body,
                                           dry_run=True)
print(result)

res = {
    'multicast_ids': [-1],
    'success': 0,
    'failure': 1,
    'canonical_ids': 0,
    'results': [{'error': 'InvalidRegistration'}],
    'topic_message_id': None
}

pl = {
    "android": {"priority": "high"},
    "dry_run": True,
    "notification": {
        "title": "Uber update",
        "body": "Hi john, your customized news for today is ready"
    },
    "to": "9WNAyu45m-RHB9VA9aT2XzQnePEgbegFHxdlbuFXB7MELt_JFVm7faFYUIrPYoHcXsRmDoMrBV4SHA0Kjm-y215"
          "vf_Uz1-1j6e933hbYXtVEsX6gMwyU0_eWSy2KrSpYfxVwLZoN_VdrYi9cYb/retMs"
}



# # Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
# message_title = "Uber update"
# message_body = "Hope you're having fun this weekend, don't forget to check today's news"
# result = push_service.notify_multiple_devices(registration_ids=registration_ids,
#                                               message_title=message_title,
#                                               message_body=message_body)
# print(result)
