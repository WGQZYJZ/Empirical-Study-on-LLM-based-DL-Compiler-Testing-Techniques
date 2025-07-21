import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.FloatTensor([[1, 0, 0, 1], [0, 1, 1, 0]])
other = torch.FloatTensor([[0, 1, 0, 1], [1, 0, 0, 1]])
result = torch.Tensor.logical_or_(_input_tensor, other)