import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
p = 2
output_tensor = torch.Tensor.mvlgamma(input_tensor, p)