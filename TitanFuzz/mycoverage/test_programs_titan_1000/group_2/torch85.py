import torch
from torch import nn
from torch.autograd import Variable
mat1 = torch.rand(2, 3)
mat2 = torch.rand(3, 2)
input_tensor = torch.rand(2, 2)
output_tensor = torch.Tensor.addmm_(input_tensor, mat1, mat2)