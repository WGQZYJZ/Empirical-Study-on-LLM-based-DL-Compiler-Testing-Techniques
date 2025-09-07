import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, 10)
k = 2
dim = 0
keepdim = False
output_tensor = torch.Tensor.kthvalue(input_tensor, k, dim, keepdim)