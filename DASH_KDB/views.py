from django.shortcuts import render
from DASH_KDB.kdb import from_kdb


def Home(request):
    return render(request, 'Home.html', locals())

def Result(request):
    name = request.GET['Name']

    qry = f'select sum runs_off_bat, sum is_ball, aveg:(sum runs_off_bat % sum wk), no_of_matchs:(count distinct match_id) ,strike:(((sum runs_off_bat) % (sum is_ball))* 100), fours: (sum four), sixs:(sum six) from IPL where striker like "{name}"'

    res = from_kdb(qry)
    # print('##########################')
    # print(list(res.iloc[0]))

    res = res.iloc[0]

    return render(request, 'Result.html', locals())

