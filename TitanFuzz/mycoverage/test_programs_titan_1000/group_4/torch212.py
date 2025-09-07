import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(2, 2)
output = torch.tanh(data)