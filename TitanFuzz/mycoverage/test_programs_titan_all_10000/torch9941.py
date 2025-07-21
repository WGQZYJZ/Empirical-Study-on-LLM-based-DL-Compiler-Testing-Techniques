import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 5)
vec1 = torch.randn(5)
vec2 = torch.randn(5)
output_tensor = torch.Tensor.addr_(input_tensor, vec1, vec2)