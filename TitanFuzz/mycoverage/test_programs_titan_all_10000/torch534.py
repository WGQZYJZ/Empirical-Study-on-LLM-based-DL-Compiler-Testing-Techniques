import torch
from torch import nn
from torch.autograd import Variable
mat1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
mat2 = torch.tensor([[1, 2], [3, 4], [5, 6]])
result = torch.mm(mat1, mat2)
mat1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
mat2 = torch.tensor([[1, 2], [3, 4], [5, 6]])
result = torch.matmul(mat1, mat2)