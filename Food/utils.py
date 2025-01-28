from django.utils import html


class ThumbnailMixin:
    def thumbnail_tag(self):
        if hasattr(self, 'thumbnail') and self.thumbnail:
                        return html.format_html(
                "<img width=100; height=100; style='border-radius: 10px;' src='{}'>",
                self.thumbnail.url
            )
        return 'No Image'