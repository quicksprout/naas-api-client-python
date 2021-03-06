import os
from naas.client_dir import version
from naas.logger import Logger


class DefaultConfiguration:
    """
    This class is meant to store all default
    configuration options that will be utilized
    throughout the client.

    These are all overrideable through the `configure`
    interface
    """
    API_HOST = 'https://naas-api-staging.tinylab.com'
    USER_AGENT = f"NAAS Python Client {version.Client.VERSION}"
    MEDIA_TYPE = 'application/json'
    CONTENT_TYPE = 'application/json'

    @staticmethod
    def access_token():
        """
        Return the ENV access token or None

        :return: str or None
        """
        return os.environ.get('NAAS_ACCESS_TOKEN')

    @staticmethod
    def api_host():
        """
        Return the ENV API Host or the default production API host.

        :return: str
        """
        return os.environ.get("NAAS_API_HOST") or DefaultConfiguration.API_HOST

    @staticmethod
    def media_type():
        """
        Return the ENV Accept header or default constant.

        :return: str
        """
        return (os.environ.get("NAAS_MEDIA_TYPE")
                or DefaultConfiguration.MEDIA_TYPE)

    @staticmethod
    def content_type():
        """
        Return the ENV Content-Type header or default constant.

        :return: str
        """
        return (os.environ.get("NAAS_CONTENT_TYPE")
                or DefaultConfiguration.CONTENT_TYPE)

    @staticmethod
    def user_agent():
        """
        Return the ENV User-Agent header or default constant.

        :return: str
        """
        return (os.environ.get("NAAS_USER_AGENT")
                or DefaultConfiguration.USER_AGENT)

    @staticmethod
    def request_logger():
        """
        Return the Default NAAS Logger to STDOUT.
        The default logger to log requests.

        :return: Logger
        """
        return Logger(log_file=os.environ.get("NAAS_LOG_FILE"))

    @staticmethod
    def cache_logger():
        """
        Return the Default NAAS Logger to STDOUT.
        If caching is enabled, this is the default logger.

        :return: Logger
        """
        return Logger(log_file=os.environ.get("NAAS_LOG_FILE"))

    @staticmethod
    def logger():
        """
        Return the Default NAAS Logger to STDOUT.
        This is for application level logging.

        :return: Logger
        """
        return Logger(log_file=os.environ.get("NAAS_LOG_FILE"))

    @classmethod
    def connection_options(cls):
        """
        Returns a set of default connection options.
        This will be deep merged with user-specified values

        :return: dict Connection Options
        """
        return {
            'headers': {
                'accept': cls.media_type(),
                'user_agent': cls.user_agent(),
                'content_type': cls.content_type()
            }
        }
