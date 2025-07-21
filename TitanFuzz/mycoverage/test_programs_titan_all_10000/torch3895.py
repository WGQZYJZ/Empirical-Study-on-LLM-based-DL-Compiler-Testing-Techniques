import torch
from torch import nn
from torch.autograd import Variable
n = 10
d = 1.0
freq = torch.fft.fftfreq(n, d)
n = 10
d = 1.0
freq = torch.fft.rfftfreq(n, d)