import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
torch.Tensor.greater_(_input_tensor, other)
_input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
torch.Tensor.greater_equal(_input_tensor, other)