import naas

from naas.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from naas.models.subscriber_email_address import SubscriberEmailAddress
from naas.models.error import Error


class SubscriberEmailAddresses(object):
    """

    Subscriber Email Addresses
    ===============

    This returns an instance of the subscriber email addresses model
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: SubscriberEmailAddress(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    @classmethod
    def list_by_subscriber_id(cls, subscriber_id, params=None):
        """
        Helper method to retrieve from the request
        :param _id: str
        :param subscriber_id: str
        :param params: dict
        :return: SubscriberEmailAddresses
        """
        if params is None:
            params = {}

        request = naas.requests.SubscriberEmailAddresses.list_by_subscriber_id(
            subscriber_id, params)

        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
        else:
            Configuration(
                {
                    "logger": ("Failure retrieving the subscriber "
                               f"email addresses  {request.status_code}")
                }
            )
        return cls(klass_attributes)

    @classmethod
    def list(cls, params=None):
        """
        Helper method to retrieve from the request
        :param params: dict
        :return: SubscriberEmailAddresses
        """
        if params is None:
            params = {}

        request = naas.requests.SubscriberEmailAddresses.list(params)

        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
        else:
            Configuration(
                {
                    "logger": ("Failure retrieving the subscriber email addresses "
                               f"{request.status_code}")
                }
            )
        return cls(klass_attributes)

    @staticmethod
    def create(params=None):
        """
        Create a new subscriber email address
        :param params: dict
        :return: SubscriberEmailAddress
        """
        if params is None:
            params = {}

        request = naas.requests.SubscriberEmailAddresses.create(params)

        if request:
            return SubscriberEmailAddress(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages()}")

        Configuration({"logger": f"{failure_message}"})
        raise InvalidRequestError(failure_message)

    @staticmethod
    def retrieve(id, params=None):
        """
        Helper method to retrieve from the request
        :param _id: str
        :param params: dict
        :return: SubscriberEmailAddress
        """
        if params is None:
            params = {}

        request = naas.requests.SubscriberEmailAddresses.retrieve(id, params)

        if request:
            return SubscriberEmailAddress(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {id}")
            return

        Configuration(
            {
                "logger": ("Failure retrieving the subscriber email address "
                           f"{request.status_code}")
            }
        )
