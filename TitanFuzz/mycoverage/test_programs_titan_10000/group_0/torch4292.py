import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(10, 10)
value = torch.randn(1)
torch.Tensor.true_divide_(input_tensor, value)