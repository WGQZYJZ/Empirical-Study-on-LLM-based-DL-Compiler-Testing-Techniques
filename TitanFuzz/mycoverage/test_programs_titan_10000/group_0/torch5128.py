import torch
from torch import nn
from torch.autograd import Variable

x = torch.ones(2, 3, 4)
torch.fft.ifft2(x)