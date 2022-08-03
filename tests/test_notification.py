import unittest

from uptime_kuma_api import UptimeKumaException
from uptime_kuma_test_case import UptimeKumaTestCase


class TestNotification(UptimeKumaTestCase):
    def test_notification(self):
        expected_notification = {
            "name": "notification 1",
            "default": True,
            "applyExisting": True,
            "type": "PushByTechulus",
            "pushAPIKey": "123456789"
        }

        # test notification
        with self.assertRaisesRegex(UptimeKumaException, r'Invalid API key'):
            self.api.test_notification(**expected_notification)

        # add notification
        r = self.api.add_notification(**expected_notification)
        self.assertEqual(r["msg"], "Saved")
        notification_id = r["id"]

        # get notification
        notification = self.api.get_notification(notification_id)
        self.compare(notification, expected_notification)

        # get notifications
        notifications = self.api.get_notifications()
        notification = self.find_by_id(notifications, notification_id)
        self.assertIsNotNone(notification)
        self.compare(notification, expected_notification)

        # edit notification
        expected_notification["name"] = "notification 1 new"
        expected_notification["default"] = False
        expected_notification["applyExisting"] = False
        expected_notification["type"] = "PushDeer"
        expected_notification["pushdeerKey"] = "987654321"
        del expected_notification["pushAPIKey"]
        r = self.api.edit_notification(notification_id, **expected_notification)
        self.assertEqual(r["msg"], "Saved")
        notification = self.api.get_notification(notification_id)
        self.compare(notification, expected_notification)
        self.assertIsNone(notification.get("pushAPIKey"))

        # delete notification
        r = self.api.delete_notification(notification_id)
        self.assertEqual(r["msg"], "Deleted")
        with self.assertRaises(UptimeKumaException):
            self.api.delete_notification(notification_id)


if __name__ == '__main__':
    unittest.main()