import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 3)
_sorted_tensor = torch.Tensor.msort(_input_tensor)