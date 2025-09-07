import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(2, 3)
result = torch.Tensor.multiply(data, 2)
data = torch.randn(2, 3)
result = torch.Tensor.div(data, 2)