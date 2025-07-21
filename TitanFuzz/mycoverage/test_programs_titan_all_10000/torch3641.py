import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, requires_grad=True)
torch.Tensor.requires_grad(input_tensor, True)