import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4)
mat1 = torch.randn(4, 2)
mat2 = torch.randn(4, 3)
torch.Tensor.sspaddmm(input_tensor, mat1, mat2)