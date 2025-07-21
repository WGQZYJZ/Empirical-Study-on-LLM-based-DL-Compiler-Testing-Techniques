import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(1, 1)
output = torch.atanh(data)