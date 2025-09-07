import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1.0, 2.0, 3.0])
other = torch.tensor([4.0, 5.0, 6.0])
torch.special.zeta(input, other)