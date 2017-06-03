from django.shortcuts import render, redirect
from drugs.models import Entities, Drugs
from drugs.forms import EntitiesForm, DrugsForm
from django.views.generic import View
import json
from django.http import HttpResponse
# Create your views here.

class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        # Index View - uncomment lines 16-22 to show names of Drugs and Entities
        form = DrugsForm()

        # entities = Entities.objects.all()
        # drugs = Drugs.objects.all()
        content = {
        #     'form':form,
        #     'entities': entities,
        #     'drugs': drugs,
        }

        return render(request, self.template_name, content)

class EntityLookup(View):
    # Autocomplete Entity lookup
    def get(self, request):
        print(request)
        term = request.GET.get('term') #jquery-ui.autocomplete parameter
        entities = Entities.objects.filter(name__istartswith=term) #lookup for a drug
        ents = []
        for n in entities:
            #make dict with the metadatas that jquery-ui.autocomple needs (the documentation is your friend)
            dict = {'id':n.id, 'label':n.name, 'entityType':n.entity_type}
            ents.append(dict)
        return HttpResponse(json.dumps(ents))


class GetDrug(View):
    # Drug record lookup
    def get(self, request):
        entity_id = request.GET.get('id')
        drug = Drugs.objects.get(entities=entity_id)
        # Makes individual drug record
        drug_card = {
            'mainName': drug.name_main,
            'condition': drug.condition_name,
            'administrationRoute': drug.admin_route
        }
        return HttpResponse(json.dumps(drug_card))

class GetMechanism(View):
    def get(self, request):
        mechanism_id = request.GET.get('id')
        drugs = Drugs.objects.filter(entities=mechanism_id)
        # makes a list of individual drug records
        drugs_list = []
        for d in drugs:
            dict = {
                'mainName': d.name_main,
                'condition': d.condition_name,
                'administrationRoute': d.admin_route
            }
            drugs_list.append(dict)
        return HttpResponse(json.dumps(drugs_list))

# Below is used to seed DB
# class SeedDB(View):

#     def get(self, request):
#         return redirect('drugs:index')

#     def post(self, request):
#         form = DrugsForm(data=request.POST)
#         # entity = requets.POST['name']
#         if form.is_valid():
#             form.save()
#         else:
#             print("problem 73")
#         return redirect('drugs:index')

