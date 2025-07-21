import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[True, True], [False, True]])
other = torch.tensor([[True, False], [False, False]])
torch.Tensor.logical_or_(input_tensor, other)