from django.core.cache import cache
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt

from .generateGraphValidateCode import geneGraphValidateCode


# Create your views here.
@csrf_exempt
def returnImageVerifyCode(request):
    imagePath, codeStrs, imageName = geneGraphValidateCode()
    cache.set('imageVerifyCode', codeStrs, 60*5)
    # ImageShow.show(image)
    # fileName = 'verifyCode' + str(time.time()).replace('.', '') + 'png'
    response = FileResponse(open(imagePath, 'rb'))
    # response['Content-Type'] = 'application/octet-stream'
    response['Content-Type'] = 'image/jpeg'
    # response['Content-Disposition'] = 'attachment;filename="{0}"'.format(imageName).encode('utf-8').
    # decode('ISO-8859-1')
    response['Content-Disposition'] = 'inline'
    return response

