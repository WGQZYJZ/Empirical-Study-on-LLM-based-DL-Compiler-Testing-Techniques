import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
torch.Tensor.copy_(input_tensor, torch.ones(2, 3))
input_tensor = torch.randn(2, 3)
input_tensor.cpu()