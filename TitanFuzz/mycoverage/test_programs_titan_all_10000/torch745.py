import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, 10)
torch.resolve_conj(input)