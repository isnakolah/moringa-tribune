from django.test import TestCase
from .models import Editor, Article, tags


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


class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james = Editor(
            first_name='James', last_name='Muriuki', email='james@moringaschool.com')
        self.james.save()

        # Creatinga new tag and saving it
        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_article = Article(
            title='Test Article', post='This is a random test post', editor=self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)
