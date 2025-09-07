import torch
from torch import nn
from torch.autograd import Variable
mat1 = torch.rand(2, 3)
mat2 = torch.rand(3, 4)
torch.Tensor.addmm(mat1, mat1, mat2, beta=1, alpha=1)