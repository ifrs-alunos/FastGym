from django.shortcuts import render
import accounts.models as accounts_models

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

def gym_seach(request):
    if request.method == "POST":
        pass