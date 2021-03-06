import iso8601
import naas
from naas.models.links import Links
from naas.models.subscriber_email_addresses import SubscriberEmailAddresses
from naas.models.project_properties import ProjectProperties
from naas.models.subscriber_project_properties import SubscriberProjectProperties
from naas.models.project_subscriber_profile import ProjectSubscriberProfile
from naas.models.project_subscriber_properties import ProjectSubscriberProperties


class ProjectSubscriber(object):
    """

    ProjectProperty
    ===============

    This returns an instance of the Project Subscriber domain model
    """

    def __init__(self, attributes={}):
        self.attributes = attributes

    def id(self):
        """Returns the id"""
        return self.attributes.get('id')

    def project_id(self):
        """Returns the associated project id"""
        return self.attributes.get('project_id')

    def subscriber_id(self):
        """Returns the associated subscriber id"""
        return self.attributes.get('subscriber_id')

    def subscriber_attributes(self):
        """Returns the eager loaded subscriber attributes"""
        return self.attributes.get('subscriber', {})

    def subscriber(self):
        """Returns the associated subscriber"""
        if self.subscriber_attributes():
            return naas.models.Subscriber(self.subscriber_attributes())
        return naas.models.Subscribers.retrieve(self.subscriber_id())

    def code(self):
        """Returns the project subscriber code"""
        return self.attributes.get('code')

    def subscriber_email_addresses_attributes(self):
        """Returns the subscriber email addresses attributes"""
        return self.attributes.get('subscriber_email_addresses', [])

    def subscriber_email_addresses(self):
        """Returns the collection of subscriber email addresses"""
        return SubscriberEmailAddresses(
            self.subscriber_email_addresses_attributes())

    def subscriber_email_addresses_display_name(self):
        return self.subscriber_email_addresses()

    def project_subscriber_properties_attributes(self):
        """Returns the project subscriber properties attributes"""
        return self.attributes.get('project_subscriber_properties', [])

    def project_subscriber_properties(self):
        """Returns the associated project subscriber properties"""
        if self.project_subscriber_properties_attributes():
            return ProjectSubscriberProperties(self.project_subscriber_properties_attributes())
        return ProjectSubscriberProperties.list_by_project_id_and_project_subscriber_id(
            self.project_id(), self.id()
        )

    def project_properties(self):
        """Returns the set of available project properties"""
        return ProjectProperties.list_by_project_id(self.project_id())

    def subscriber_project_properties(self):
        """
        This returns a collection of all project properties merged with the
        values set by this subscriber

        @note: This is a WIP to test out this model
        """
        records = []
        for project_property in self.project_properties().collection:
            record_attributes = {
                "project_property_id": project_property.id(),
                "project_subscriber_property_id":  None,
                "name":  project_property.name(),
                "key_name": project_property.key_name(),
                "description": project_property.description(),
                "value ": None,
                "is_subscriber_editable": project_property.is_subscriber_editable(),
                "is_subscriber_viewable": project_property.is_subscriber_viewable()
            }

            subscriber_value = None

            for i in self.project_subscriber_properties.collection:
                if i.project_property_id() == project_property.id():
                    subscriber_value = i
                    break

            if subscriber_value:
                subscriber_attributes = {
                    "project_subscriber_property_id": subscriber_value.id(),
                    "value": subscriber_value.value(),
                    "is_subscriber_editable": subscriber_value.is_subscriber_editable()
                }
                record_attributes.update(subscriber_attributes)
            records.append(record_attributes)
        return SubscriberProjectProperties(records)

    def profile_attributes(self):
        """Returns the profile attributes"""
        return self.attributes.get('profile', {})

    def profile(self):
        """Returns an instance of the profile"""
        if self.profile_attributes():
            return ProjectSubscriberProfile(self.profile_attributes())
        return ProjectSubscriberProfile.retrieve_by_project_id_and_project_subscriber_id(
            self.project_id(), self.id()
        )

    def is_opted_in(self):
        """Returns true if opted in to the project"""
        return self.attributes.get('is_opted_in')

    def opted_in_at(self):
        """Returns the date they opted in to the project"""
        return iso8601.parse_date(self.attributes.get('opted_in_at'))

    def opted_out_at(self):
        """Returns the date they opted out of the project"""
        return iso8601.parse_date(self.attributes.get('opted_out_at'))

    def created_at(self):
        """Returns the created at timestamp value"""
        return iso8601.parse_date(self.attributes.get('created_at'))

    def updated_at(self):
        """Returns the updated at timestamp value"""
        return iso8601.parse_date(self.attributes.get('updated_at'))

    def links_attributes(self):
        """Returns the links attributes"""
        return self.attributes.get('links', [])

    def links(self):
        """Returns links"""
        return Links(self.links_attributes())

    def to_a(self):
        """Serialized the record as an array"""
        return [
            self.id(), self.project_id(), self.subscriber_id(),
            self.subscriber_email_addresses_display_name(), self.code(),
            self.created_at()
        ]
