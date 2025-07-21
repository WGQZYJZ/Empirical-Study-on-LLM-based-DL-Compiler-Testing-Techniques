import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 3)
mat = torch.randn(3, 4)
vec = torch.randn(4)
torch.Tensor.addmv_(input_tensor, mat, vec)