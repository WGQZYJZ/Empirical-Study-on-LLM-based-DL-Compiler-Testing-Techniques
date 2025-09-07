import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(5, 3, requires_grad=True)
torch.Tensor.sinh_(input_tensor)