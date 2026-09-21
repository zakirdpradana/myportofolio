from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateTimeInput, CharField, PasswordInput, DateInput

from main.models import Experience, Education

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

class EducationForm(ModelForm):
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
        model = Education
        fields = [
            "institution_name",
            "description",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "institution_name": "Nama Institusi Pendidikan",
            "description": "Deskripsi Pendidikan",
            "thumbnail": "URL Logo Institusi Pendidikan",
            "started_at": "Tanggal Mulai",
            "ended_at": "Tanggal Selesai (Kosongkan jika masih berlangsung)",
        }

        widgets = {
            "institution_name": TextInput(
                attrs={
                    "placeholder": "SMA 67 Jakarta",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                        "placeholder": "Jelaskan program studi, perjalanan, atau pencapaianmu",
                        "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "started_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }