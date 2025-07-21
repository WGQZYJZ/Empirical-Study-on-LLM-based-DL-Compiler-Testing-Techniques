import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
vec = torch.randn(4)
output_tensor = torch.Tensor.mv(input_tensor, vec)