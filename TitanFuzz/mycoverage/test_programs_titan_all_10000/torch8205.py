import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1, 0, 1], [0, 1, 0]])
other = torch.tensor([[0, 1, 0], [1, 0, 1]])
result = torch.Tensor.logical_and(_input_tensor, other)