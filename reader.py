import pickle
import generator
output = open('meta.data','wb')
imgPath = "200000.jpg"
data = generator.export(imgPath)
pickle.dump(data,output)
output.close
