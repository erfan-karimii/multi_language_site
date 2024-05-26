from django.shortcuts import render
from django.utils.translation import gettext_lazy as _ , pgettext_lazy


def index_page(request):
    success_message = _('yeeeh yo did it!')
    month  = pgettext_lazy('month name','may')
    may = p('possibility','may')
    return render(request,'index.html',{"success_message":success_message,"month":month,"may":may})
