from django.core.management.base import BaseCommand
from home_server.models import ClientUser
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
import os
from django.conf import settings
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        old = tuple(i["codename"] for i in Permission.objects.values("codename"))

        ct = ContentType.objects.get_for_model(ClientUser)

        
        location = settings.BASE_DIR/"Permissions"
        
        # Permission.objects.filter(content_type=ct).delete()
        # print(location)
        # location = os.path.join(settings.BASE_DIR, 'technical', 'permissions', 'operator_permissions.json')       
        for files in os.listdir(location):
            with open(location / files) as per_file:
                per = json.load(per_file)["Permissions"]

            for i in per:
                if not i["name"] in old:
                    Permission.objects.create(
                        name=i["des"],
                        codename=i["name"],
                        content_type=ct
                    )
        print("created")
