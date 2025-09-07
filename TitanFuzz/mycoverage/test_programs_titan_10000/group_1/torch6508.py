import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(3, 4)
logcumsumexp_tensor = torch.Tensor.logcumsumexp(input_tensor, dim=1)