from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            "movie_id", "movie_title", "actor1_name", "actor2_name",
            "director_name", "movie_genre", "release_year",
        ]

    def clean(self):
        data = super().clean()
        a1, a2 = data.get("actor1_name"), data.get("actor2_name")
        if a1 and a2 and a1.strip().lower() == a2.strip().lower():
            raise forms.ValidationError("Actor1 and Actor2 cannot be the same.")
        return data
