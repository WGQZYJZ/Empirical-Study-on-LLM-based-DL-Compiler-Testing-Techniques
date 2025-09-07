import torch
from torch import nn
from torch.autograd import Variable
mat = torch.randn(4, 3)
vec = torch.randn(3)
out = torch.zeros(4)
torch.Tensor.addmv_(out, mat, vec)
mat = torch.randn(4, 3)
vec = torch.randn(3)
out = torch.zeros(4)
torch.Tensor.addmv_(out, mat, vec, beta=2, alpha=0.5)