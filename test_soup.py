import re
from bs4 import BeautifulSoup
import requests
from general_utils import measure_time
# https://medex.com.bd/brands/10929/a-fenac-25mg

# for atr in soup.find_all(href=re.compile("/brands/")):
#     print(atr["href"])


def find_content(soup, content_id):
    final_content = None
    content = soup.find(id=content_id)
    if content:
        parent = content.parent
        final_content = parent.find_all('div')[1].text

    return final_content


def get_page_urls(base_url, limit):
    return [f'{base_url}?page={page_num}' for page_num in range(1,limit+1)]

@measure_time
def collect_medicine_info_from_medex(base_url='https://medex.com.bd/brands', limit=1):
    page_url_list = get_page_urls(base_url,limit)
    for idx,page_url in enumerate(page_url_list):
        res = requests.get(page_url)
        soup = BeautifulSoup(res.content, 'html.parser')
        print(f"For Page {idx+1}\n")
        for atr in soup.find_all(href=re.compile("/brands/"))[:]:
            medicine_url = atr['href']
            print(f"Details of {medicine_url.split('/')[-1]}")
            res2 = requests.get(medicine_url)
            soup2 = BeautifulSoup(res2.content, 'html.parser')
            full = soup2.find( "h1","page-heading-1-l" ).find_all("span")[1].text

            dosage = soup2.find( "h1","page-heading-1-l" ).find_all("span")[1].small.text
            brand_name = full.replace(dosage, "").strip()
            generic_name =soup2.find(attrs={"title": "Generic Name"}).a.text.strip()
            strength = soup2.find(attrs={"title": "Strength"}).text.strip()
            manufactured_by = soup2.find(attrs={"title": "Manufactured by"}).a.text.strip()
            package_container = "".join(soup2.find(attrs={"class": "package-container"}).text.strip().split())
            indications = find_content(soup=soup2, content_id='indications')
            therapheutic_class = find_content(soup=soup2, content_id='drug_classes')
            description = find_content(soup=soup2, content_id='description')
            pharmacology = find_content(soup=soup2, content_id='mode_of_action')
            doasge_and_administration = find_content(soup=soup2, content_id='dosage')
            interaction = find_content(soup=soup2, content_id='interaction')
            contraindications = find_content(soup=soup2, content_id='contraindications')
            side_effects = find_content(soup=soup2, content_id='side_effects')
            pregnancy_and_lactation = find_content(soup=soup2, content_id='pregnancy_cat')
            precautions = find_content(soup=soup2, content_id='precautions')
            storage_conditions = find_content(soup=soup2, content_id='storage_conditions')
            overdose_effects = find_content(soup=soup2, content_id='overdose_effects')
            administration = find_content(soup=soup2, content_id='administration')

            print(f"Brand: {brand_name}\nDosage form: {dosage}\nGeneric Name: {generic_name}\nStrength: {strength}\n"
                  f"Manufactured By: {manufactured_by}\nPackage: {package_container}\nIndications: {indications}\n"
                  f"Therapheutic Class: {therapheutic_class}\nDescription: {description}\nPharmacology: {pharmacology}\n"
                  f"Dosage&Administration: {doasge_and_administration}\nInteraction: {interaction}\nContraindications: {contraindications}\n"
                  f"Side Effects: {side_effects}\nPregnancy and Lactation: {pregnancy_and_lactation}\nPrecautions: {precautions}\n"
                  f"Storage Conditions: {storage_conditions}\nOverdose_effects: {overdose_effects}\nAdministration: {administration}")
            print('\n\n\n')


        print('\n\n\n')


if __name__ == '__main__':
    collect_medicine_info_from_medex(limit=1)
