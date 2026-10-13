# Shrine of Order model: core/weapon stats lose at most 25; attunements can drop to the average;
# stats below the level are raised to it; leftover points are returned free.
CORE={'STR','FTD','AGL','INT','WLL','CHA','MED','HVY','LHT'}
def shrine(pre):
    inv={k:v for k,v in pre.items() if v>0}
    P=sum(inv.values())
    best=None
    for L in range(0,101):
        tot=0; post={}
        for k,v in inv.items():
            if v>L:
                post[k]=max(L,v-25) if k in CORE else L
            else:
                post[k]=L
            tot+=post[k]
        if tot<=P: best=(L,post,P-tot)
        else: break
    return best
if __name__=='__main__':
    import sys,json
    pre=json.loads(sys.argv[1]); print(shrine(pre))
