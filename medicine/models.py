from django.db import models
from django.urls import reverse




class Medicine(models.Model): #model for Medicine Products

	dosage = models.CharField(max_length=50)
	brand_name = models.CharField(max_length=100)
	generic_name = models.CharField(max_length=500)
	strength = models.FloatField()
	manufactured_by = models.CharField(max_length=500)
	unit_price = models.FloatField()
	indications = models.TextField(blank=True)
	therapheutic_class = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	pharmacology = models.TextField(blank=True)
	doasge_and_administration = models.TextField(blank=True)
	interaction = models.TextField(blank=True)
	contraindications = models.TextField(blank=True)
	side_effects = models.TextField(blank=True)
	pregnancy_and_lactation = models.TextField(blank=True)
	precautions = models.TextField(blank=True)
	storage_conditions = models.TextField(blank=True)
	overdose_effects = models.TextField(blank=True)
	administration = models.TextField(blank=True)


	class Meta:
		ordering = ('brand_name',)
		verbose_name = 'medicine'
		verbose_name_plural = 'medicines'

	def get_url(self):
		return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])

	def __str__(self):
		return '{}'.format(self.name)
