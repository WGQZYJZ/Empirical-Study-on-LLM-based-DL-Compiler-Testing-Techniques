import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 4, 4, requires_grad=True)
output = torch.nn.functional.softsign(input)