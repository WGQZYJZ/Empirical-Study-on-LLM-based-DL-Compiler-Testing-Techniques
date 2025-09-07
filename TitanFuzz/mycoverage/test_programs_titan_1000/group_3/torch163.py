import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(100)
histogram = torch.Tensor.histogram(input_tensor, bins=10)