import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 3)
torch.Tensor.cov(input_tensor)