import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10)
hist = torch.Tensor.histogram(input_tensor, input_tensor, bins=10)