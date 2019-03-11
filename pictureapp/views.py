from django.http  import Http404
# Create your views here.
@login_required(login_url='/accounts/login/')
def user_page(request):
    date = dt.date.today()
    current_user = request.user
    followed_people= []
    images1 =[]
    following  = Follow.objects.filter(follower = current_user)
    is_following = Follow.objects.filter(follower = current_user).count()
    try:
        if is_following != 0:
            for folling_object in following:
                image_set = Profile.objects.filter(id = folling_object.user.id)
                for item in image_set:
                    followed_people.append(item)
            for followed_profile in followed_people:
                post = Image.objects.filter(user_key = followed_profile.user)
                for item in post:
                    images1.append(item)
                    images= list(reversed(images1))
            return render(request, 'my-grams/user_page.html',{"date":date,"user_page_images":images})
    except:
        raise Http404
    return render(request, 'my-grams/startup.html')
