import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 5)
torch.Tensor.transpose_(input_tensor, 0, 1)