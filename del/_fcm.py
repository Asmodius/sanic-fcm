from .baseapi import BaseAPI
# from .errors import InvalidDataError


class FCMNotification(BaseAPI):
    def notify_single_device(self,
                             registration_id=None,
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
                             android_channel_id=None,
                             timeout=5,
                             extra_notification_kwargs=None):
        """
        Send push notification to a single device

        :param str registration_id: FCM device registration IDs.
        :param str message_body: Message string to display in the notification tray.
        :param str message_title: The notification's title. This field is not visible on iOS phones
            and tablets.
        :param str message_icon: The notification's icon. Sets the notification icon to MyIcon for
            drawable resource MyIcon. If you don't send this key in the request, FCM displays the
            launcher icon specified in your app manifest.
        :param str sound: The sound file name to play. Specify "Default" for device default sound.
        :param str condition: This parameter specifies a logical expression of conditions that
            determine the message target. Supported condition: Topic, formatted as "'yourTopic' in
            topics". This value is case-insensitive. Supported operators: &&, ||. Maximum two
            operators per topic message supported.
        :param str collapse_key: Identifier for a group of messages that can be collapsed so that
            only the last message gets sent when delivery can be resumed. Defaults to ``None``.
        :param bool delay_while_idle: If ``True`` indicates that the message should not be sent
            until the device becomes active.
        :param int time_to_live: How long (in seconds) the message should be kept in FCM storage if
            the device is offline. The maximum time to live supported is 4 weeks. Defaults to
            ``None`` which uses the FCM default of 4 weeks.
        :param str restricted_package_name: Package name of the application where the registration
            IDs must match in order to receive the message. Defaults to ``None``.
        :param bool low_priority: Whether to send notification with the low priority flag.
        :param bool dry_run: If ``True`` no message will be sent but request will be tested.
        :param dict data_message: Data message payload to send alone or with the notification
            message
        :param click_action:
        :param badge:
        :param color:
        :param tag:
        :param body_loc_key:
        :param body_loc_args:
        :param title_loc_key:
        :param title_loc_args:
        :param content_available:
        :param str android_channel_id: new in Android O.
        :param int timeout: set time limit for the request.
        :param extra_notification_kwargs:
        :return dict `multicast_id(long), success(int), failure(int), canonical_ids(int),
            results(list)`: Response from FCM server.
        :raise AuthenticationError: If :attr:`api_key` is not set or provided or there is an error
            authenticating the sender.
        :raise FCMServerError: Internal server error or timeout error on Firebase cloud messaging
            server.
        :raise InvalidDataError: Invalid data provided
        :raise InternalPackageError: Mostly from changes in the response of FCM, contact the project
            owner to resolve the issue.
        """
#         if registration_id is None:
#             raise InvalidDataError('Invalid registration ID')
#         # [registration_id] cos we're sending to a single device
#         payload = self.parse_payload(registration_ids=[registration_id],
#                                      message_body=message_body,
#                                      message_title=message_title,
#                                      message_icon=message_icon,
#                                      sound=sound,
#                                      condition=condition,
#                                      collapse_key=collapse_key,
#                                      delay_while_idle=delay_while_idle,
#                                      time_to_live=time_to_live,
#                                      restricted_package_name=restricted_package_name,
#                                      low_priority=low_priority,
#                                      dry_run=dry_run, data_message=data_message,
#                                      click_action=click_action,
#                                      badge=badge,
#                                      color=color,
#                                      tag=tag,
#                                      body_loc_key=body_loc_key,
#                                      body_loc_args=body_loc_args,
#                                      title_loc_key=title_loc_key,
#                                      title_loc_args=title_loc_args,
#                                      android_channel_id=android_channel_id,
#                                      content_available=content_available,
#                                      extra_notification_kwargs=extra_notification_kwargs)
#
#         self.send_request([payload], timeout)
#         return self.parse_responses()

    def single_device_data_message(self,
                                   registration_id=None,
                                   condition=None,
                                   collapse_key=None,
                                   delay_while_idle=False,
                                   time_to_live=None,
                                   restricted_package_name=None,
                                   low_priority=False,
                                   dry_run=False,
                                   data_message=None,
                                   content_available=None,
                                   android_channel_id=None,
                                   timeout=5,
                                   extra_notification_kwargs=None):
        """
        Send push message to a single device.

        :param str registration_id: FCM device registration IDs.
        :param str condition:
        :param str collapse_key: Identifier for a group of messages that can be collapsed so that
            only the last message gets sent when delivery can be resumed. Defaults to ``None``.
        :param bool delay_while_idle: If ``True`` indicates that the message should not be sent
            until the device becomes active.
        :param int time_to_live: How long (in seconds) the message should be kept in FCM storage if
            the device is offline. The maximum time to live supported is 4 weeks. Defaults to
            ``None`` which uses the FCM default of 4 weeks.
        :param str restricted_package_name: Package name of the application where the registration
            IDs must match in order to receive the message. Defaults to ``None``.
        :param bool low_priority: Whether to send notification with the low priority flag.
        :param bool dry_run: If ``True`` no message will be sent but request will be tested.
        :param dict data_message: Data message payload to send alone or with the notification
            message.
        :param content_available:
        :param str android_channel_id: new in Android O
        :param int timeout: set time limit for the request
        :param extra_notification_kwargs:
        :return dict:`multicast_id(long), success(int), failure(int), canonical_ids(int),
            results(list)`: Response from FCM server.
        :raise AuthenticationError: If :attr:`api_key` is not set or provided or there is an error
            authenticating the sender.
        :raise FCMServerError: Internal server error or timeout error on Firebase cloud messaging
            server.
        :raise InvalidDataError: Invalid data provided.
        :raise InternalPackageError: Mostly from changes in the response of FCM, contact the
            project owner to resolve the issue.
        """
#         if registration_id is None:
#             raise InvalidDataError('Invalid registration ID')
#         # [registration_id] cos we're sending to a single device
#         payload = self.parse_payload(registration_ids=[registration_id],
#                                      condition=condition,
#                                      collapse_key=collapse_key,
#                                      delay_while_idle=delay_while_idle,
#                                      time_to_live=time_to_live,
#                                      restricted_package_name=restricted_package_name,
#                                      low_priority=low_priority,
#                                      dry_run=dry_run,
#                                      data_message=data_message,
#                                      content_available=content_available,
#                                      remove_notification=True,
#                                      android_channel_id=android_channel_id,
#                                      extra_notification_kwargs=extra_notification_kwargs)
#
#         self.send_request([payload], timeout)
#         return self.parse_responses()

    def notify_multiple_devices(self,
                                registration_ids=None,
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
                                android_channel_id=None,
                                timeout=5,
                                extra_notification_kwargs=None):
        """
        Sends push notification to multiple devices, can send to over 1000 devices.

        :param str registration_ids: FCM device registration IDs.
        :param str message_body: Message string to display in the notification tray.
        :param str message_title:
        :param str message_icon:
        :param sound: The sound file name to play. Specify "Default" for device default sound.
        :param str condition:
        :param str collapse_key: Identifier for a group of messages that can be collapsed so that
            only the last message gets sent when delivery can be resumed.
        :param bool delay_while_idle: If ``True`` indicates that the message should not be sent
            until the device becomes active.
        :param int time_to_live: How long (in seconds) the message should be kept in FCM storage
            if the device is offline. The maximum time to live supported is 4 weeks. Defaults to
            ``None`` which uses the FCM default of 4 weeks.
        :param str restricted_package_name: Package name of the application where the registration
            IDs must match in order to receive the message. Defaults to ``None``.
        :param bool low_priority: Whether to send notification with the low priority flag.
        :param bool dry_run: If ``True`` no message will be sent but request will be tested.
        :param dict data_message: Data message payload to send alone or with the notification
            message.
        :param click_action:
        :param badge:
        :param color:
        :param tag:
        :param body_loc_key:
        :param body_loc_args:
        :param title_loc_key:
        :param title_loc_args:
        :param content_available:
        :param str android_channel_id: new in Android O.
        :param timeout:
        :param extra_notification_kwargs:
        :return tuple:`multicast_id(long), success(int), failure(int), canonical_ids(int),
            results(list)`: Response from FCM server.
        :raise AuthenticationError: If :attr:`api_key` is not set or provided or there is an error
            authenticating the sender.
        :raise FCMServerError: Internal server error or timeout error on Firebase cloud messaging
            server.
        :raise InvalidDataError: Invalid data provided.
        :raise InternalPackageError: JSON parsing error, mostly from changes in the response of FCM,
            create a new github issue to resolve it.
        """
#         payloads = []
#         registration_id_chunks = self.registration_id_chunks(registration_ids)
#         for registration_ids in registration_id_chunks:
#             # appends a payload with a chunk of registration ids here
#             payloads.append(self.parse_payload(registration_ids=registration_ids,
#                                                message_body=message_body,
#                                                message_title=message_title,
#                                                message_icon=message_icon,
#                                                sound=sound,
#                                                condition=condition,
#                                                collapse_key=collapse_key,
#                                                delay_while_idle=delay_while_idle,
#                                                time_to_live=time_to_live,
#                                                restricted_package_name=restricted_package_name,
#                                                low_priority=low_priority,
#                                                dry_run=dry_run, data_message=data_message,
#                                                click_action=click_action,
#                                                badge=badge,
#                                                color=color,
#                                                tag=tag,
#                                                body_loc_key=body_loc_key,
#                                                body_loc_args=body_loc_args,
#                                                title_loc_key=title_loc_key,
#                                                title_loc_args=title_loc_args,
#                                                content_available=content_available,
#                                                android_channel_id=android_channel_id,
#                                                extra_notification_kwargs=extra_notification_kwargs))
#         self.send_request(payloads, timeout)
#         return self.parse_responses()
#
    def multiple_devices_data_message(self,
                                      registration_ids=None,
                                      condition=None,
                                      collapse_key=None,
                                      delay_while_idle=False,
                                      time_to_live=None,
                                      restricted_package_name=None,
                                      low_priority=False,
                                      dry_run=False,
                                      data_message=None,
                                      content_available=None,
                                      timeout=5,
                                      extra_notification_kwargs=None):
        """
        Sends push message to multiple devices, can send to over 1000 devices.

        :param str registration_ids: FCM device registration IDs.
        :param str condition:
        :param str collapse_key: Identifier for a group of messages that can be collapsed so that
            only the last message gets sent when delivery can be resumed.
        :param bool delay_while_idle: If ``True`` indicates that the message should not be sent
            until the device becomes active.
        :param int time_to_live: How long (in seconds) the message should be kept in FCM storage if
            the device is offline. The maximum time to live supported is 4 weeks. Defaults to
            ``None`` which uses the FCM default of 4 weeks.
        :param str restricted_package_name: Package name of the application where the registration
            IDs must match in order to receive the message. Defaults to ``None``.
        :param bool low_priority: Whether to send notification with the low priority flag.
        :param bool dry_run: If ``True`` no message will be sent but request will be tested.
        :param dict data_message: Data message payload to send alone or with the notification
            message.
        :param content_available:
        :param timeout:
        :param extra_notification_kwargs:
        :return tuple:`multicast_id(long), success(int), failure(int), canonical_ids(int),
            results(list)`: Response from FCM server.
        :raise AuthenticationError: If :attr:`api_key` is not set or provided or there is an error
            authenticating the sender.
        :raise FCMServerError: Internal server error or timeout error on Firebase cloud messaging
            server.
        :raise InvalidDataError: Invalid data provided.
        :raise InternalPackageError: JSON parsing error, mostly from changes in the response of FCM,
            create a new github issue to resolve it.
        """
#         payloads = list()
#         registration_id_chunks = self.registration_id_chunks(registration_ids)
#         for registration_ids in registration_id_chunks:
#             # appends a payload with a chunk of registration ids here
#             payloads.append(self.parse_payload(registration_ids=registration_ids,
#                                                condition=condition,
#                                                collapse_key=collapse_key,
#                                                delay_while_idle=delay_while_idle,
#                                                time_to_live=time_to_live,
#                                                restricted_package_name=restricted_package_name,
#                                                low_priority=low_priority,
#                                                dry_run=dry_run,
#                                                data_message=data_message,
#                                                content_available=content_available,
#                                                remove_notification=True,
#                                                extra_notification_kwargs=extra_notification_kwargs))
#         self.send_request(payloads, timeout)
#         return self.parse_responses()
#
    def notify_topic_subscribers(self,
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
                                 android_channel_id=None,
                                 timeout=5,
                                 extra_notification_kwargs=None):
        """
        Sends push notification to multiple devices subscribed to a topic.
        :param str topic_name: Name of the topic to deliver messages to condition (condition):
            Topic condition to deliver messages to A topic name is a string that can be formed with
            any character in [a-zA-Z0-9-_.~%].
        :param str message_body: Message string to display in the notification tray.
        :param str message_title:
        :param str message_icon:
        :param str sound: The sound file name to play. Specify "Default" for device default sound.
        :param condition:
        :param str collapse_key: Identifier for a group of messages that can be collapsed so that
            only the last message gets sent when delivery can be resumed.
        :param bool delay_while_idle: If ``True`` indicates that the message should not be sent
            until the device becomes active.
        :param int time_to_live: How long (in seconds) the message should be kept in FCM storage if
            the device is offline. The maximum time to live supported is 4 weeks. Defaults to
            ``None`` which uses the FCM default of 4 weeks.
        :param str restricted_package_name: Package name of the application where the registration
            IDs must match in order to receive the message.
        :param bool low_priority: Whether to send notification with the low priority flag.
        :param bool dry_run: If ``True`` no message will be sent but request will be tested.
        :param dict data_message: Data message payload to send alone or with the notification
            message.
        :param click_action:
        :param badge:
        :param color:
        :param tag:
        :param body_loc_key:
        :param body_loc_args:
        :param title_loc_key:
        :param title_loc_args:
        :param content_available:
        :param str android_channel_id: new in Android O.
        :param timeout:
        :param extra_notification_kwargs:
        :return tuple:`multicast_id(long), success(int), failure(int), canonical_ids(int),
            results(list)`: Response from FCM server.
        :raise AuthenticationError: If :attr:`api_key` is not set or provided or there is an error
            authenticating the sender.
        :raise FCMServerError: Internal server error or timeout error on Firebase cloud messaging
            server.
        :raise InvalidDataError: Invalid data provided.
        :raise InternalPackageError: JSON parsing error, mostly from changes in the response of FCM,
            create a new github issue to resolve it.
        """
#         payload = self.parse_payload(topic_name=topic_name,
#                                      condition=condition,
#                                      message_body=message_body,
#                                      message_title=message_title,
#                                      message_icon=message_icon,
#                                      sound=sound,
#                                      collapse_key=collapse_key,
#                                      delay_while_idle=delay_while_idle,
#                                      time_to_live=time_to_live,
#                                      restricted_package_name=restricted_package_name,
#                                      low_priority=low_priority,
#                                      dry_run=dry_run, data_message=data_message,
#                                      click_action=click_action,
#                                      badge=badge,
#                                      color=color,
#                                      tag=tag,
#                                      body_loc_key=body_loc_key,
#                                      body_loc_args=body_loc_args,
#                                      title_loc_key=title_loc_key,
#                                      title_loc_args=title_loc_args,
#                                      content_available=content_available,
#                                      android_channel_id=android_channel_id,
#                                      extra_notification_kwargs=extra_notification_kwargs)
#         self.send_request([payload], timeout)
#         return self.parse_responses()
