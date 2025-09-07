import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4, 4)
cov = torch.Tensor.cov(input_tensor)