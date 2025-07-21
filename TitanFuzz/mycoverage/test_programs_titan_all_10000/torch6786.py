import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
mat1 = torch.tensor([[1, 2], [3, 4], [5, 6]])
mat2 = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.sspaddmm(input_tensor, mat1, mat2)