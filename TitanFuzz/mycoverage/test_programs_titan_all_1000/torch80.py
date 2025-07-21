import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(1, 10)
torch.cos(data, out=None)