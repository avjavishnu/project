from django.shortcuts import render
from django.http import HttpResponse
import pickle
# Create your views here.

def index(request):
    return render(request,'chatapp/index.html')


def getResponse(request):
    userM=request.GET.get('userMessage')
    #print(userM)
    vtrfile=open("vtr.sav","rb")
    vtrfile=pickle.load(vtrfile)

    csyfile=open("csy.sav","rb")
    csyfile=pickle.load(csyfile)

    npfile=open("np.sav","rb")
    npfile=pickle.load(npfile)

    vqfile=open("vq.sav","rb")
    vqfile=pickle.load(vqfile)

    dffile=open("df.sav","rb")
    dffile=pickle.load(dffile)
    user_input =userM
    vectorized_user_input = vtrfile.transform([user_input])

    similarities = csyfile(vectorized_user_input,
                                     vqfile)

    closest_question = npfile(similarities,
                                    axis=1)

    ##print("Similarities: ", similarities)

    ##print("Closest question: ", closest_question)

    answer = dffile.Answer.iloc[closest_question].values[0]
    answer=answer.title()
    print(answer)
    return HttpResponse(answer)




    #userM=userM.capitalize()
    #return HttpResponse(userM)
