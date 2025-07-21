import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 3, 3)
torch.nn.functional.rrelu_(input)