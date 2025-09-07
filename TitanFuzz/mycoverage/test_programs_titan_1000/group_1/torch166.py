import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(100)
torch.Tensor.expm1_(input_tensor)