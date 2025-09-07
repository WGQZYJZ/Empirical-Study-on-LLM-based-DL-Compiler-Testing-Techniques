import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, requires_grad=True)
torch.Tensor.sign_(input_tensor)