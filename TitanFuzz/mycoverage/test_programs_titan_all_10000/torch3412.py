import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3)
mat2 = torch.rand(3, 2)
output_tensor = torch.Tensor.mm(_input_tensor, mat2)