import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4, 4)
torch.Tensor.clip(input_tensor, min=(- 0.5), max=0.5)