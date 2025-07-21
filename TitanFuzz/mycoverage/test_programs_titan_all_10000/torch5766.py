import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 2, 3, 4, 5)
p = 2
output_tensor = torch.Tensor.mvlgamma(input_tensor, p)