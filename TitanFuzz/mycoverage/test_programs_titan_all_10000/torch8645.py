import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10)
p = 0.5
output_tensor = torch.Tensor.geometric_(input_tensor, p)