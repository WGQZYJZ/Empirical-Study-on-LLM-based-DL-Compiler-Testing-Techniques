import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
torch.Tensor.clamp_(input_tensor, min=(- 0.5), max=0.5)