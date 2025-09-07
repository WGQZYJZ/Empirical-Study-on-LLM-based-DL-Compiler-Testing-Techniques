import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4, 4)
value = 2
torch.Tensor.true_divide_(input_tensor, value)
input_tensor = torch.randn(4, 4)
torch.Tensor.trunc_(input_tensor)