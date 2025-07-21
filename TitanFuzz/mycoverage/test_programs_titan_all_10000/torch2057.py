import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[True, False, True], [True, True, False], [False, False, False]])
other = torch.tensor([[True, True, False], [False, False, False], [True, True, True]])
result = torch.Tensor.logical_and_(input_tensor, other)