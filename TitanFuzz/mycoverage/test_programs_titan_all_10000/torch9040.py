import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10)
torch.Tensor.cos_(input_tensor)