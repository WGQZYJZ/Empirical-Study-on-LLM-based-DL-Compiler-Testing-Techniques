import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(4)
output = torch.asinh(data)