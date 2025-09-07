import torch
from torch import nn
from torch.autograd import Variable
mat1 = torch.randn(3, 4)
mat2 = torch.randn(4, 5)
torch.Tensor.mm(mat1, mat2)
torch.mm(mat1, mat2)