import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
torch.Tensor.transpose_(input_tensor, 0, 1)
torch.Tensor.transpose_(input_tensor, 1, 0)