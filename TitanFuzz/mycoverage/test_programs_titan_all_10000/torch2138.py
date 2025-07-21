import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 10)
torch.Tensor.arctan_(input_tensor)