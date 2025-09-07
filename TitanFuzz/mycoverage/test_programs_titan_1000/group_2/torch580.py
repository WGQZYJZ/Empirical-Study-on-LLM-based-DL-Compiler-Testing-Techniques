import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(3, 3)
resolve_conj = torch.resolve_conj(input)