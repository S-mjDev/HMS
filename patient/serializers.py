from django.contrib.auth.models import Group, User
from patient.models import Patient
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        # expose the primary key so clients can see the record ID
        fields = ["url", "id", "firstname", "midname", "lastname", "address", "birthday", "age", "consultation_date", "doctor", "medical_history"]

<<<<<<< HEAD
    def validate(self, data):
        firstname = data.get("firstname")
        midname = data.get("midname")
        lastname = data.get("lastname")
        birthday = data.get("birthday")

        if firstname and lastname:
            query = Patient.objects.filter(
                firstname__iexact=firstname.strip(),
                lastname__iexact=lastname.strip(),
            )

            if midname:
                query = query.filter(midname__iexact=midname.strip())

            if birthday:
                query = query.filter(birthday=birthday)

            if self.instance and self.instance.pk:
                query = query.exclude(pk=self.instance.pk)

            if query.exists():
                raise serializers.ValidationError({
                    "non_field_errors": [
                        "A patient with the same name and birthday already exists."
                    ]
                })

        return data

=======
>>>>>>> 507d7d53ae00c78e08bb362c85ad854ae7affc73
