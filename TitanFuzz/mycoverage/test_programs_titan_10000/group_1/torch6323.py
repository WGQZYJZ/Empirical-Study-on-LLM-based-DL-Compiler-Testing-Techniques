import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(3, 4)
mat = torch.randn(4, 3)
output = torch.Tensor.smm(input_tensor, mat)