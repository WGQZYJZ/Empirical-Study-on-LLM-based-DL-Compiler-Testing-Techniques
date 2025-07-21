import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 10)
vec1 = torch.randn(10)
vec2 = torch.randn(10)
output = torch.Tensor.addr(input_tensor, vec1, vec2)