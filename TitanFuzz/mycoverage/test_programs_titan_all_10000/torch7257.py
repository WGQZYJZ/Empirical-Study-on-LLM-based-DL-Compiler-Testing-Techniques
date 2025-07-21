import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2], [3, 4]])
mat2 = torch.Tensor([[1, 2], [3, 4]])
output_tensor = torch.Tensor.mm(input_tensor, mat2)