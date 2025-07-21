import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(1, 1, 4))
torch.nn.AdaptiveMaxPool1d(1, return_indices=False)