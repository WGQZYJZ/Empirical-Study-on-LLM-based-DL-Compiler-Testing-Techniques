import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(4, 4, 4)
dim = 1
index = torch.tensor([0, 1, 2, 3])
src = torch.randn(4, 4, 4)
_output_tensor = torch.Tensor.scatter(_input_tensor, dim, index, src)