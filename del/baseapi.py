# import json
# import time
#
# from .errors import (AuthenticationError, InvalidDataError, FCMError, InternalPackageError,
#                      FCMServerError)


class BaseAPI(object):
    """
    Base class for the afcm API wrapper for FCM
    """
#     CONTENT_TYPE = "application/json"
#     FCM_END_POINT = "https://fcm.googleapis.com/fcm/send"
#     FCM_MAX_RECIPIENTS = 1000  # FCM only allows up to 1000 reg ids per bulk message.
#
#     def __init__(self, api_key):
#         self._FCM_API_KEY = api_key
#         self.requests_session = requests.Session()
#         self.send_request_responses = []
#
#     def request_headers(self):
#         return {
#             "Content-Type": self.CONTENT_TYPE,
#             "Authorization": "key=" + self._FCM_API_KEY,
#         }
#
#     def registration_id_chunks(self, registration_ids):
#         """Yield successive 1000-sized (max fcm recipients per request) chunks from
#         registration_ids."""
#         for i in range(0, len(registration_ids), self.FCM_MAX_RECIPIENTS):
#             yield registration_ids[i:i + self.FCM_MAX_RECIPIENTS]
#
#     @staticmethod
#     def json_dumps(data):
#         """Standardized json.dumps function with separators and sorted keys set."""
#         return json.dumps(data, separators=(',', ':'), sort_keys=True).encode('utf8')

    def parse_payload(self,
                      registration_ids=None,
                      topic_name=None,
                      message_body=None,
                      message_title=None,
                      message_icon=None,
                      sound=None,
                      condition=None,
                      collapse_key=None,
                      delay_while_idle=False,
                      time_to_live=None,
                      restricted_package_name=None,
                      low_priority=False,
                      dry_run=False,
                      data_message=None,
                      click_action=None,
                      badge=None,
                      color=None,
                      tag=None,
                      body_loc_key=None,
                      body_loc_args=None,
                      title_loc_key=None,
                      title_loc_args=None,
                      content_available=None,
                      remove_notification=False,
                      extra_notification_kwargs: dict = None,
                      **extra_kwargs):
#         fcm_payload = {}
#         ...
#
#         if delay_while_idle:
#             fcm_payload['delay_while_idle'] = delay_while_idle
#         ...
#         if restricted_package_name:
#             fcm_payload['restricted_package_name'] = restricted_package_name
#         ...
#
#         fcm_payload['notification'] = {}
#         if message_icon:
#             fcm_payload['notification']['icon'] = message_icon
#         # If body is present, use it
#         if message_body:
#             fcm_payload['notification']['body'] = message_body
#         # Else use body_loc_key and body_loc_args for body
#         else:
#             if body_loc_key:
#                 fcm_payload['notification']['body_loc_key'] = body_loc_key
#             if body_loc_args:
#                 if isinstance(body_loc_args, list):
#                     fcm_payload['notification']['body_loc_args'] = body_loc_args
#                 else:
#                     raise InvalidDataError('body_loc_args should be an array')
#         # If title is present, use it
#         if message_title:
#             fcm_payload['notification']['title'] = message_title
#         # Else use title_loc_key and title_loc_args for title
#         else:
#             if title_loc_key:
#                 fcm_payload['notification']['title_loc_key'] = title_loc_key
#             if title_loc_args:
#                 if isinstance(title_loc_args, list):
#                     fcm_payload['notification']['title_loc_args'] = title_loc_args
#                 else:
#                     raise InvalidDataError('title_loc_args should be an array')
#
#         # This is needed for iOS when we are sending only custom data messages
#         if content_available and isinstance(content_available, bool):
#             fcm_payload['content_available'] = content_available
#
#         if click_action:
#             fcm_payload['notification']['click_action'] = click_action
#         if isinstance(badge, int) and badge >= 0:
#             fcm_payload['notification']['badge'] = badge
#         if color:
#             fcm_payload['notification']['color'] = color
#         if tag:
#             fcm_payload['notification']['tag'] = tag
#         # only add the 'sound' key if sound is not None
#         # otherwise a default sound will play -- even with empty string args.
#         if sound:
#             fcm_payload['notification']['sound'] = sound
#
#         if extra_kwargs:
#             fcm_payload.update(extra_kwargs)
#
#         if extra_notification_kwargs:
#             fcm_payload['notification'].update(extra_notification_kwargs)
#
#         # Do this if you only want to send a data message.
#         if remove_notification:
#             del fcm_payload['notification']
#
#         return self.json_dumps(fcm_payload)

#     def registration_info_request(self, registration_id):
#         """ Makes a request for registration info and returns the response
#             object
#         """
#         response = self.requests_session.get(
#             'https://iid.googleapis.com/iid/info/' + registration_id,
#             params={'details': 'true'})
#         return response
#
#     def clean_registration_ids(self, registration_ids=None):
#         """ Return list of active IDS from the list of registration_ids
#         """
#         valid_registration_ids = []
#         for registration_id in (registration_ids or []):
#             details = self.registration_info_request(registration_id)
#             if details.status_code == 200:
#                 valid_registration_ids.append(registration_id)
#         return valid_registration_ids
#
#     def get_registration_id_info(self, registration_id):
#         """ Returns details related to a registration id if it exists
#             otherwise return None
#         """
#         details = self.registration_info_request(registration_id)
#         if details.status_code == 200:
#             return details.json()
#         return None
#
#     def subscribe_registration_ids_to_topic(self, registration_ids, topic_name):
#         """ Subscribes a list of registration ids to a topic
#         """
#         url = '''https://iid.googleapis.com/iid/v1:batchAdd'''
#         payload = json.dumps({
#             'to': '/topics/' + topic_name,
#             'registration_tokens': registration_ids,
#         })
#         response = self.requests_session.post(url, data=payload)
#         if response.status_code == 200:
#             return True
#         elif response.status_code == 400:
#             error = json.loads(response.content)
#             raise InvalidDataError(error['error'])
#         else:
#             raise FCMError()
#
#     def unsubscribe_registration_ids_from_topic(self, registration_ids, topic_name):
#         """ Unsubscribe a list of registration ids from a topic."""
#         url = '''https://iid.googleapis.com/iid/v1:batchRemove'''
#         payload = json.dumps({
#             'to': '/topics/' + topic_name,
#             'registration_tokens': registration_ids,
#         })
#         response = self.requests_session.post(url, data=payload)
#         if response.status_code == 200:
#             return True
#         elif response.status_code == 400:
#             error = json.loads(response.content)
#             raise InvalidDataError(error['error'])
#         else:
#             raise FCMError()
