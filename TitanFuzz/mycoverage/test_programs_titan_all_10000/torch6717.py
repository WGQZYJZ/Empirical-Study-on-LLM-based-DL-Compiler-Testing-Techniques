import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4)
dim = 0
index = 1
output_tensor = torch.Tensor.select(input_tensor, dim, index)