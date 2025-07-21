import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 5, requires_grad=True)
other = torch.randn(3, 5, requires_grad=True)
torch.Tensor.xlogy_(input_tensor, other)