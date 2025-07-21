import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 3)
A = torch.randn(3, 3)
torch.Tensor.solve(_input_tensor, A)