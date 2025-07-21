import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 5)
other = torch.randn(5, 4)
torch.Tensor.dot(_input_tensor, other)