import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 2, 2))
torch.nn.functional.rrelu_(input, lower=(1.0 / 8), upper=(1.0 / 3), training=False)