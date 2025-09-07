import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(100, 10)
torch.Tensor.cov(input_tensor)