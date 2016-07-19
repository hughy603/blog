from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog.blog'
    verbose_name = "Blog"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
