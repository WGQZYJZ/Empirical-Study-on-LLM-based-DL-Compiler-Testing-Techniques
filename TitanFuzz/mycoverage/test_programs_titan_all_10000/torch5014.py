import torch
from torch import nn
from torch.autograd import Variable
y = torch.randn(1, 5)
trapz = torch.trapz(y)