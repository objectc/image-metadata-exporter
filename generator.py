from PIL import Image
infoKey = {'width','height','filename'}
def export(fn):
    ret = {}
    i = Image.open(fn)
    
    for key in infoKey:
        ret[key] = getattr(i,key)
    return ret
