import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3)
vec2 = torch.rand(3)
output_tensor = torch.Tensor.ger(input_tensor, vec2)