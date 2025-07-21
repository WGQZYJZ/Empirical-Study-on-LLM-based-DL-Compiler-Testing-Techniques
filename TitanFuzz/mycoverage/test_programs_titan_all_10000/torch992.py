import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
output = torch.nn.functional.rrelu_(input, lower=(1.0 / 8), upper=(1.0 / 3), training=False)