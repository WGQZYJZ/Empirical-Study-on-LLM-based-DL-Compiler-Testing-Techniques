import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
torch.all(input, dim=0)
torch.all(input, dim=1)