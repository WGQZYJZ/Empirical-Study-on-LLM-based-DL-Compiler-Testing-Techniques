import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, requires_grad=True)
torch.Tensor.retains_grad(input_tensor, True)