import iso8601

from naas.models import (
    Links, EmailNotificationStatuses, EmailNotificationDeliveries
)
from naas.requests import EmailNotificationStatuses as notification_status


class EmailNotification(object):
    """

    Email Notification
    ===============

    This returns an instance of the Email Notification domain model
    """

    def __init__(self, attributes={}):
        self.attributes = attributes

    def id(self):
        """Returns the subscriber id"""
        return self.attributes.get('id')

    def deliver(self):
        """Deliver for this instance"""
        return EmailNotifications.deliver(self.id)

    def delivery_status(self):
        """Returns the delivery status"""
        status = notification_status.retrieve_by_email_notification_id(self.id)
        if status:
            return EmailNotificationStatuses.retrieve_by_email_notification_id(
                self.id)
        return status

    def email_notification_deliveries(params={}):
        """Returns the Email Notification Deliveries"""
        if self.email_notification_deliveries_attributes():
            return EmailNotificationDeliveries(
                self.email_notification_deliveries_attributes())
        return EmailNotificationDeliveries.list_by_email_notification_id(
            self.id, params)

    def email_notification_deliveries_count(self):
        """Returns the count of the email notification deliveries"""
        return len(self.email_notification_deliveries())

    def email_notification_deliveries_attributes(self):
        """Returns the email notification deliveries attributes"""
        return self.attributes.get('email_notification_deliveries')

    def account_smtp_setting_id(self):
        """Returns the account smtp setting id"""
        return self.attributes.get('account_smtp_setting_id')

    def campaign_email_template_id(self):
        """Returns the campaign email template id"""
        return self.attributes.get('campaign_email_template_id')

    def subscriber_email_address_id(self):
        """Returns the subscriber email address id"""
        return self.attributes.get('subscriber_email_address_id')

    def content(self):
        """Returns the content"""
        return self.attributes.get('content')

    def subject(self):
        """Returns the subject"""
        return self.attributes.get('subject')

    def from_email_address(self):
        """Returns the from email address"""
        return self.attributes.get('from_email_address')

    def from_name(self):
        """Returns the from name"""
        return self.attributes.get('from_name')

    def to_email_address(self):
        """Returns the to email address"""
        return self.attributes.get('to_email_address')

    def to_name(self):
        """Returns the to name"""
        return self.attributes.get('to_name')

    def html_body(self):
        """Returns the html_body"""
        return self.attributes.get('html_body')

    def text_body(self):
        """Returns the text body"""
        return self.attributes.get('text_body')

    def sent_count(self):
        """Returns the sent count"""
        return self.attributes.get('sent_count', 0)

    def is_processing(self):
        """Returns true if processing"""
        return self.attributes.get('is_processing', False)

    def is_deliverable(self):
        """Returns true if this is deliverable"""
        return self.attributes.get('is_deliverable', False)

    def checksum(self):
        """Returns the checksum of the content"""
        return self.attributes.get('checksum')

    def last_sent_at(self):
        """Returns the last sent at timestamp"""
        return iso8601.parse_date(self.attributes.get('last_sent_at'))

    def created_at(self):
        """Returns the created at timestamp"""
        return iso8601.parse_date(self.attributes.get('created_at'))

    def updated_at(self):
        """Returns the updated at timestamp"""
        return iso8601.parse_date(self.attributes.get('updated_at')

    def links_attributes(self):
        """Returns the links attributes"""
        return self.attributes.get('links', [])

    def links(self):
        return Links(self.links_attributes())