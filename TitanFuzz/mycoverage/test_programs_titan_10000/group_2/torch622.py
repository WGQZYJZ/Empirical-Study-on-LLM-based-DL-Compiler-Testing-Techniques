import torch
from torch import nn
from torch.autograd import Variable

y = torch.randn(3, 4)
z = torch.trapz(y)