import torch
from torch import nn
from torch.autograd import Variable
mat1 = torch.Tensor([[1, 2], [3, 4]])
mat2 = torch.Tensor([[5, 6], [7, 8]])
torch.Tensor.mm(mat1, mat2)