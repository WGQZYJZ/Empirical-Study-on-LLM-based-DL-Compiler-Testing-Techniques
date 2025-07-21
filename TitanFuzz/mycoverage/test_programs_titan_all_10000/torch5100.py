import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(2, 3)
other = torch.rand(2, 3)
torch.allclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)