import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
mat1 = torch.randn(3, 3)
mat2 = torch.randn(3, 3)
output_tensor = torch.Tensor.sspaddmm(input_tensor, mat1, mat2, beta=1, alpha=1)