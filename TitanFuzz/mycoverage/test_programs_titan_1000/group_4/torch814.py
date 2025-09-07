import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10)
torch.Tensor.lgamma_(input_tensor)