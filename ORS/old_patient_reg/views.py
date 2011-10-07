# Create your views here.

import csv 
from django.http import HttpResponse

def exportdata(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=orsdata.csv'

    writer = csv.writer(response)
    writer.writerow(['forst row', 'foo', 'tes',])

    return response
