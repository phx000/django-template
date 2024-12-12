import uuid

from django.db import connection, models
from django.db.models.base import ModelBase
from django.db.utils import ProgrammingError
from django.test import TestCase


class AbstractModelBaseTestCase(TestCase):
    """
    Base class for tests of model mixins/abstract models.
    To use, subclass and specify the mixin class variable.
    A model using the mixin will be made available in self.model
    """

    @classmethod
    def setUpTestData(cls):
        # Create a dummy model which extends the mixin. A RuntimeWarning will
        # occur if the model is registered twice
        if not hasattr(cls, "abstract_class"):
            raise NotImplementedError("Subclasses must define a 'abstract_class' attribute.")

        if not hasattr(cls, 'model'):
            cls.model = ModelBase(
                '__TestModel__' + cls.abstract_class.__name__+f"_{uuid.uuid4().hex}",
                (cls.abstract_class,),
                {'__module__': cls.abstract_class.__module__,}
            )

        # Create the schema for our test model. If the table already exists,
        # will pass
        try:
            with connection.schema_editor() as schema_editor:
                schema_editor.create_model(cls.model)
            super().setUpTestData()
        except ProgrammingError:
            pass

    @classmethod
    def tearDownClass(self):
        # Delete the schema for the test model. If no table, will pass
        try:
            with connection.schema_editor() as schema_editor:
                schema_editor.delete_model(self.model)
            super().tearDownClass()
        except ProgrammingError:
            pass
