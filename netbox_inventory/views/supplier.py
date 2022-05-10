from netbox.views import generic
from utilities.utils import count_related
from .. import filtersets, forms, models, tables

__all__ = (
    'SupplierView',
    'SupplierListView',
    'SupplierEditView',
    'SupplierDeleteView',
    #'SupplierBulkImportView',
    #'SupplierBulkEditView',
    'SupplierBulkDeleteView',
)

class SupplierView(generic.ObjectView):
    queryset = models.Supplier.objects.all()


class SupplierListView(generic.ObjectListView):
    queryset = models.Supplier.objects.annotate(
        asset_count=count_related(models.Asset, 'supplier'),
    )
    table = tables.SupplierTable
    filterset = filtersets.SupplierFilterSet
    #filterset_form = forms.SupplierFilterForm


class SupplierEditView(generic.ObjectEditView):
    queryset = models.Supplier.objects.all()
    form = forms.SupplierForm


class SupplierDeleteView(generic.ObjectDeleteView):
    queryset = models.Supplier.objects.all()


# class SupplierBulkImportView(generic.BulkImportView):
#     queryset = models.Supplier.objects.all()   
#     table = tables.SupplierTable 
#     model_form = forms.SupplierCSVForm


# class SupplierBulkEditView(generic.BulkEditView):
#     queryset = models.Supplier.objects.all()
#     filterset = filtersets.SupplierFilterSet
#     table = tables.SupplierTable
#     form = forms.SupplierBulkEditForm


class SupplierBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Supplier.objects.all()
    table = tables.SupplierTable
