import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(4, 3, 3)
output = torch.Tensor.diagonal(input_tensor)