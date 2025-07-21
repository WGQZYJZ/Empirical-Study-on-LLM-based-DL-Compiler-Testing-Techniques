import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
mat1 = torch.randn(3, 4)
mat2 = torch.randn(4, 5)
result = torch.Tensor.addmm(input_tensor, mat1, mat2)