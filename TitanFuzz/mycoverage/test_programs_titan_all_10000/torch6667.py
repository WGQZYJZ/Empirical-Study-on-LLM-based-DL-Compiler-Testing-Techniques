import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(2, 3)
output = torch.jit.isinstance(data, torch.Tensor)