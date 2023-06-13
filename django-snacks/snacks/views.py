# What is going to be invoked when the user visits your website?

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
            {
                "title": "Hawaiian BBQ chips",
                "description": "Solid snack, one of my favorites",
            }, {
                "title": "Beef jerky",
                "description": "Also very solid, but have to be in the mood",
            }, {
                "title": "Ramen",
                "description": "More of a meal than a snack, solid",
            }
        ]

        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ImagePageView(TemplateView):
    template_name = 'image.html'
