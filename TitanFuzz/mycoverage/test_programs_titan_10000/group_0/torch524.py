import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.rand(2, 3)
_neg_tensor = torch.Tensor.neg(_input_tensor)