import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
p = 2
output_tensor = torch.Tensor.mvlgamma_(input_tensor, p)