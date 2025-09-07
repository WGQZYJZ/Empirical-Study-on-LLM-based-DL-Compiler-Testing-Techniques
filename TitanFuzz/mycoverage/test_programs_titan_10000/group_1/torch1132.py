import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4, 4)
torch.Tensor.requires_grad_(input_tensor, requires_grad=True)