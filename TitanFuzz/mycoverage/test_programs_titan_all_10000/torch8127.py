import torch
from torch import nn
from torch.autograd import Variable
mat1 = torch.rand((3, 4))
mat2 = torch.rand((4, 5))
mat3 = torch.rand((3, 5))
result = torch.Tensor.sspaddmm(mat3, mat1, mat2, beta=1, alpha=1)