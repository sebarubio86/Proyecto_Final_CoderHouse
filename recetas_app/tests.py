from django.test import TestCase
from .forms import RecetaForm
from .models import Receta
"""
# Create your tests here.
class RecetaModelTestCase(TestCase):
    def creacion_receta(self):
        Receta.objects.create(nombre="Pizza", descripcion="La mejor pizza la argentina, mejor que la italiana por lejos")
        self.assertEqual(Receta.objects.count(), 1)


    def lectura_receta(self):
        Receta.objects.create(nombre="Pizza", descripcion="La mejor pizza la argentina, mejor que la italiana por lejos")
        recetas = Receta.objects.all()
        self.assertGreaterEqual(len(recetas), 1)


    def modificacion_receta(self):
        Receta.objects.update(nombre="Pizza", descripcion="La mejor pizza la argentina, la mejor del mundo mundial")
        recetas = Receta.objects.all()
        print(recetas)

"""

class RecetaFormTest(TestCase):
    
    def test_valid_form(self):
        form_data = {'nombre': 'Pizza', 'descripcion': 'La mejor pizza la argentina, mejor que la italiana por lejos'}
        form = RecetaForm(data=form_data)
        print(form)
        print(self.assertTrue(form.is_valid()))

    def test_invalid_form(self):
        form_data = {'nombre': None, 'descripcion': 'La mejor pizza la argentina, mejor que la italiana por lejos'}
        form = RecetaForm(data=form_data)
        print(form)
        print(self.assertFalse(form.is_valid()))
