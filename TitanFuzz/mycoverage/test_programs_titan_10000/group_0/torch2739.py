import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.rand(10, 3)
torch.Tensor.msort(_input_tensor)