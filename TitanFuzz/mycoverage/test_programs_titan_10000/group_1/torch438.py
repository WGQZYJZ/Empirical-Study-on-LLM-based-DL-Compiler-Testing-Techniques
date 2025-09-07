import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.Tensor([1, 2, 3, 4])
_other = torch.Tensor([5, 6, 7, 8])
torch.Tensor.igammac(_input_tensor, _other)