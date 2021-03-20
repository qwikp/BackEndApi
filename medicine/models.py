from django.db import models
from django.urls import reverse




class Medicine(models.Model): #model for Medicine Products

	dosage = models.CharField(max_length=50,blank=True,null=True)
	brand_name = models.CharField(max_length=100,blank=True,null=True)
	generic_name = models.CharField(max_length=500,null=True,blank=True)
	strength = models.FloatField(default=0)
	manufactured_by = models.CharField(max_length=500,null=True,blank=True)
	unit_price = models.FloatField(default=0)
	indications = models.TextField(blank=True,null=True)
	therapheutic_class = models.CharField(max_length=100,null=True,blank=True)
	description = models.TextField(blank=True,null=True)
	pharmacology = models.TextField(blank=True,null=True)
	doasge_and_administration = models.TextField(blank=True,null=True)
	interaction = models.TextField(blank=True,null=True)
	contraindications = models.TextField(blank=True,null=True)
	side_effects = models.TextField(blank=True,null=True)
	pregnancy_and_lactation = models.TextField(blank=True,null=True)
	precautions = models.TextField(blank=True,null=True)
	storage_conditions = models.TextField(blank=True,null=True)
	overdose_effects = models.TextField(blank=True,null=True)
	administration = models.TextField(blank=True,null=True)


	class Meta:
		ordering = ('brand_name',)
		verbose_name = 'medicine'
		verbose_name_plural = 'medicines'


	def __str__(self):
		return '{}'.format(self.brand_name)
