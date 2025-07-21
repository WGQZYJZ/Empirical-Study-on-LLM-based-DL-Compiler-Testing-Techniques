import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(100, 100)
torch.Tensor.cosh_(input_tensor)