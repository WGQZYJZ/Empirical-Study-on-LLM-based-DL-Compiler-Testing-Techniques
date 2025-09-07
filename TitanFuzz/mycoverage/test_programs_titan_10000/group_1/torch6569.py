import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4, 4)
p = torch.randn(4, 4)
torch.Tensor.mvlgamma_(input_tensor, p)