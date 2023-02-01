from django.urls import path, re_path
from django.conf.urls import include

from documentos.views import DocAnalisisView, DocPruebasUniView, DocRequisitosView, DocRegistroRastreoView, DocPruebasView

urlpatterns = [
    re_path(r'doc_analisis$', DocAnalisisView.as_view()),
    re_path(r'doc_pruebas_uni$', DocPruebasUniView.as_view()),
    re_path(r'doc_requisitos$', DocRequisitosView.as_view()),
    re_path(r'doc_registro_rastreo$', DocRegistroRastreoView.as_view()),
    re_path(r'doc_pruebas$', DocPruebasView.as_view()),
]