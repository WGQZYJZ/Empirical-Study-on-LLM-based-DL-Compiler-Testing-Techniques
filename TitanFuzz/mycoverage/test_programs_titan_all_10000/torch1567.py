import torch
from torch import nn
from torch.autograd import Variable
n = torch.tensor(4)
d = torch.tensor(1)
x = torch.fft.rfftfreq(n, d)