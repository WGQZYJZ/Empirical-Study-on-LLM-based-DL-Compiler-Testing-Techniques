import torch
from torch import nn
from torch.autograd import Variable
mat1 = torch.randn(3, 3)
mat2 = torch.randn(3, 3)
mat3 = torch.randn(3, 3)
torch.Tensor.addmm_(mat1, mat2, mat3)