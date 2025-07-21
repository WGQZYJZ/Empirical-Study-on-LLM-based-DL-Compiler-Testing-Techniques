import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
divisor = torch.randn(2, 3)
torch.Tensor.fmod_(input_tensor, divisor)