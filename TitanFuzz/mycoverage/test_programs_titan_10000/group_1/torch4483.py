import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(3, 3)
p = 2
result = torch.Tensor.mvlgamma(input_tensor, p)