import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4, 5)
torch.Tensor.geometric_(input_tensor, 0.5)