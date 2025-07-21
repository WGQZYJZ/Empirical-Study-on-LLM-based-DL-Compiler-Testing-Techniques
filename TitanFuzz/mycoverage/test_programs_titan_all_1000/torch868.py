import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(100, 100)
result = torch.Tensor.erfinv_(data)