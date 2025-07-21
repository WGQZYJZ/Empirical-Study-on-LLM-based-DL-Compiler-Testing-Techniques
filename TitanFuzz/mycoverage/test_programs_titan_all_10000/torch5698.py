import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(5, 5)
vec1 = torch.rand(5)
vec2 = torch.rand(5)
output_tensor = torch.Tensor.addr(input_tensor, vec1, vec2)