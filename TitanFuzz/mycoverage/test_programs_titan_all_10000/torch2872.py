import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 3, 3)
other = torch.randn(1, 1, 3, 3)
torch.allclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)
input = torch.randn(1, 1, 3, 3)
other = torch.randn(1, 1, 3, 3)
torch.allclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)