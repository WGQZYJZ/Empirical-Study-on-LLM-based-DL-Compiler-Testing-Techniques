import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3)
mat1 = torch.rand(2, 3)
mat2 = torch.rand(3, 3)
torch.Tensor.addmm(input_tensor, mat1, mat2)