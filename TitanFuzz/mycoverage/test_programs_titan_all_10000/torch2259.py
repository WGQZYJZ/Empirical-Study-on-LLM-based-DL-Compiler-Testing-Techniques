import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3, requires_grad=True)
input = (input + input.conj())
output = torch.resolve_conj(input)