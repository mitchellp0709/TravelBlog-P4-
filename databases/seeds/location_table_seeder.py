"""LocationTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Location import Location


class LocationTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Location.create({"name":"Italy","description":"loved it there","visited":True,"image":"https://cdn.britannica.com/82/195482-050-2373E635/Amalfi-Italy.jpg"})
        Location.create({"name":"France","description":"can't wait to go","visited":False,"image":"https://static.independent.co.uk/2021/03/11/13/iStock-1185953092.jpg?width=982&height=726&auto=webp&quality=75"})
        Location.create({"name":"England","description":"yay england","visited":True,"image":"https://cdn.hswstatic.com/gif/UK-Britain-1.jpg"})
        Location.create({"name":"Spain","description":"my dream place","visited":False,"image":"https://i.natgeofe.com/k/e800ca90-2b5b-4dad-b4d7-b67a48c96c91/spain-madrid_16x9.jpg?w=1200"})
