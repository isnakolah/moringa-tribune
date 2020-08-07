from django.test import TestCase
from .models import Editor, Article, Tags


class EditorTextClass(TestCase):

    # Set up method
    def setUp(self):
        self.james = Editor(
            first_name='James', last_name='Muriuki', email='james@moringaschool.com')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james, Editor))

    # Testing saving method
    def test_save_editor(self):
        self.james.save()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    # Testing deleting a Editor
    def test_delete_editor(self):
        self.james.save()
        Editor.objects.get(first_name='James').delete()
        self.assertTrue(len(Editor.objects.all()) == 0)

    # Test for displaying all model objects saved
    def test_for_displaying_all_model_objects_saved(self):
        self.james.save()
        kimkay = Editor.objects.create(
            first_name='Kim', last_name='Kardashian', email='kimkay@gmail.com')
        self.assertEqual(len(Editor.objects.all()), 2)

    # Test for updating single object properties
    def test_for_updating_single_object_properties(self):
        self.james.save()
        Editor.objects.filter(first_name='James').update(first_name='Daniel')
        self.assertEqual(Editor.objects.all()[0].first_name, 'Daniel')
