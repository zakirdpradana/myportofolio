from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateTimeInput, CharField, PasswordInput

from main.models import Experience

class ExperienceForm(ModelForm):
    secret_key = CharField(
        label = "Kode Rahasia Admin",
        widget = PasswordInput(
            attrs={
                "placeholder": "Masukkan kode rahasia"
            }
        ),
        required = True
    )

    class Meta:
        model = Experience
        fields = [
            "title",  
            "description",
            "category", 
            "thumbnail", 
            "ended_at",
        ]

        labels = {
            "title": "Nama Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "thumbnail": "URL Gambar Thumbnail",
            "ended_at": "Tanggal & Waktu Selesai (Kosongkan jika masih berlangsung)",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Software Engineering Intern",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                        "placeholder": "Jelaskan peran dan tanggung jawabmu",
                        "rows": 3,
                }
            ),
            "category": Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
        }
        