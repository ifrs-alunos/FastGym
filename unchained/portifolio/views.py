from django.shortcuts import render
import accounts.models as accounts_models
from .forms import Search

def gym_view(request, gym_id):
    gym = accounts_models.Gym.objects.get(id=gym_id)
    context = {
        'gym_name' : gym.owner.first_name,
        'gym_email': gym.owner.email,
        'gym_telefone' : gym.telefone,
        'gym_cnpj' : gym.cnpj,
        'gym_endereco': gym.endereco,
        'gym_associados': str(gym.associados)
    }
    return render(request, "portfolio/gym.html", context)

def gym_search(request):
    form = Search()
    context = {
        'init':True,
        'form': form,
    }
    if request.method == "POST":
        formulario = Search(request.POST)
        if formulario.is_valid():
            search = formulario.cleaned_data['text']
            print(search)
            results = set()
            for x in search.split():
                cidade = accounts_models.Gym.objects.filter(cidade__contains=x)
                estado = accounts_models.Gym.objects.filter(estado__contains=x)
                for y in cidade:
                    results.add(y)
                for z in estado:
                    results.add(z)
            print(results)
            context['init'] = False
            context['form'] = Search()
            if len(results) >= 1:
                context['academias'] = results
            else:
                context['no_results'] = True

    return render(request, "portfolio/search.html", context)