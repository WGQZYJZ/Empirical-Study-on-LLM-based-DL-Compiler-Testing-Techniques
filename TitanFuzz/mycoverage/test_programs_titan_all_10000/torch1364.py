import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 4)
mat1 = torch.rand(4, 5)
mat2 = torch.rand(5, 3)
output_tensor = torch.Tensor.sspaddmm(input_tensor, mat1, mat2)