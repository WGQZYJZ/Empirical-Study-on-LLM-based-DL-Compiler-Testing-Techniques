import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 10)
histogram_output = torch.Tensor.histogram(input_tensor, bins=10)