import torch
from torch import nn
from torch.autograd import Variable
input = torch.Tensor([[0.1, 0.2, 0.3, 0.4]])
torch.multinomial(input, 2)
torch.multinomial(input, 3, replacement=True)