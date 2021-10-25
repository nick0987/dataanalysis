import pandas
import numpy 
from scipy.stats import norm
#reading data from the file
Data = pandas.read_excel('data_200010040.xlsx',header = None)
Data_val = Data.values
#First 1000 values sepeeated as noise 
Noise = Data_val[:1000]
#Next 10000 values received by one of the two friends
received_signal = Data_val[1000:]
Exnoise = numpy.mean(Noise)
Exre_signal = numpy.mean(received_signal)
#avg value of trans_sinal will be avg value of re_signal-avg value of noise
Extrans_signal = Exre_signal - Exnoise
#bias without accounting error
bias1 = Extrans_signal/5
#error1:tail received as head due to noise
error1=1-norm.cdf((Exre_signal-Exnoise)/numpy.std(Noise))#converting noise as standard normal distribution 
noisenew=(Noise-Exnoise)/numpy.std(Noise)
#error2:head received as tail due to noise
error2=norm.cdf((Exre_signal-5-Exnoise)/numpy.std(Noise))
#bias on accounting error
bias=bias1-(bias1*error1) + (bias1*error2)
print("Bias of coin is:",round(bias, 1))