import torch
from torch import nn
from torch.autograd import Variable
x = np.arange(0, 10)
freq = torch.fft.rfftfreq(10, d=1.0)