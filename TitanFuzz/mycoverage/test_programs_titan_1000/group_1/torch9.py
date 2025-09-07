import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.Tensor([[1, 0, 1], [0, 1, 1]])
other = torch.Tensor([[0, 1, 1], [0, 1, 0]])
torch.Tensor.logical_xor_(_input_tensor, other)