from qpython import qconnection

def from_kdb(inp):
    try:
        q = qconnection.QConnection(host = 'localhost', port = 5001,timeout = 3.0, pandas = True)
        q.open()
        #res = q.sendSync('select sum runs_off_bat, sum is_ball, aveg:(sum runs_off_bat % sum wk), no_of_matchs:(count distinct match_id) ,strike:(((sum runs_off_bat) % (sum is_ball))* 100), fours: (sum four), sixs:(sum six) from IPL where striker like "Sourav Ganguly"')
        res = q.sendSync(inp)
        return res
    except:
        return "Having some error"
    
#select sum runs_off_bat, sum is_ball, aveg:(sum runs_off_bat % sum wk), no_of_matchs:(count distinct match_id) ,strike:(((sum runs_off_bat) % (sum is_ball))* 100), fours: (sum four), sixs:(sum six) from IPL where striker like "Sourav Ganguly"
