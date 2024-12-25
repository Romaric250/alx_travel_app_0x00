from django.core.management.base import BaseCommand
from listings.models import Property, User
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        host = User.objects.filter(role='host').first()
        if not host:
            self.stdout.write(self.style.ERROR('No host user found. Create a host first.'))
            return

        for i in range(10):
            Property.objects.create(
                host=host,
                name=f"Property {i+1}",
                description=f"Description for property {i+1}",
                location=f"Location {i+1}",
                price_per_night=random.uniform(50, 500)
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with sample properties.'))
