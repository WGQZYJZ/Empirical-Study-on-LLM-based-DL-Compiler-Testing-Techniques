import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 3)
vec2 = torch.rand(4)
result = torch.Tensor.ger(input_tensor, vec2)