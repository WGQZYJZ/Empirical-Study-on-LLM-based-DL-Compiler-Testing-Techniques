import torch
from torch import nn
from torch.autograd import Variable
input = torch.Tensor([[0.1, 0.2, 0.3, 0.4, 0.5]])
output = torch.multinomial(input, 2, replacement=False)