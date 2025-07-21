import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[True, False], [True, True]])
other = torch.tensor([[True, False], [False, False]])
torch.Tensor.logical_and_(_input_tensor, other)