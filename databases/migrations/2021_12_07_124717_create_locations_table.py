"""CreateLocationsTable Migration."""

from masoniteorm.migrations import Migration


class CreateLocationsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("locations") as table:
            table.increments("id")
            table.string("name")
            table.string("description")
            table.string("image")
            table.boolean("visited")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("locations")
