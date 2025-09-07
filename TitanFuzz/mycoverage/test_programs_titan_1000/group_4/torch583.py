import torch
from torch import nn
from torch.autograd import Variable
mat = torch.randn(4, 3)
vec = torch.randn(3)
torch.Tensor.addmv_(mat, mat, vec)