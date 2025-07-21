import torch
from torch import nn
from torch.autograd import Variable
mat1 = torch.Tensor([[1, 2, 3], [4, 5, 6]])
mat2 = torch.Tensor([[1, 2], [3, 4], [5, 6]])
torch.Tensor.mm(mat1, mat2)
torch.mm(mat1, mat2)
torch.matmul(mat1, mat2)
mat1.matmul(mat2)