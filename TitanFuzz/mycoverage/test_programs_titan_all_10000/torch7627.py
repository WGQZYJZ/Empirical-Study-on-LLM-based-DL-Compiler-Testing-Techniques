import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 4)
vec2 = torch.rand(4)
output = torch.Tensor.outer(input_tensor, vec2)