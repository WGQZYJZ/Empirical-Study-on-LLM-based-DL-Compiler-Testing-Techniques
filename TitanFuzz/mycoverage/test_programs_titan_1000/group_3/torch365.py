import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 32, 32)
future = torch.jit._fork(torch.sum, input)
torch.jit.wait(future)