import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1000)
histogram = torch.Tensor.histogram(input_tensor, 10, 0, 1)