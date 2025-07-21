import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
value = 2
torch.Tensor.floor_divide_(input_tensor, value)