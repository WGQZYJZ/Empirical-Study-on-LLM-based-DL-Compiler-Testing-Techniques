import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
output = torch.randn(4, 4)
torch.special.entr(input, out=output)