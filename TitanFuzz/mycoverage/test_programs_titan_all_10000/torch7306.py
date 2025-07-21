import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3)
mat1 = torch.rand(3, 4)
mat2 = torch.rand(4, 5)
output_tensor = torch.Tensor.addmm_(input_tensor, mat1, mat2)