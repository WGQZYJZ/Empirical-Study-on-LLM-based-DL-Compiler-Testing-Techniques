import torch
from torch import nn
from torch.autograd import Variable
random.seed(0)
input = torch.randn(1, 1, 3, 3)
torch.nn.functional.rrelu_(input, lower=(1.0 / 8), upper=(1.0 / 3), training=False)