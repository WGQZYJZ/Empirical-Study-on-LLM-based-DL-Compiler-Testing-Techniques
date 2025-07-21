import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(3, 4)
output = torch.erfc(data)