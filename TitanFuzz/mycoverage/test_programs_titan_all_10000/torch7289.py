import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
torch.Tensor.float_power_(input_tensor, 2)
torch.Tensor.float_power_(input_tensor, 0.5)