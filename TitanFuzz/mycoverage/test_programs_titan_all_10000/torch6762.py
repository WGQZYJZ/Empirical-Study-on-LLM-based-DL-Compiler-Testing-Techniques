import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 5)
torch.Tensor.cos_(input_tensor)
cos_tensor = torch.cos(input_tensor)