import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 3, 3)
torch.nn.Threshold(threshold=0.5, value=0.0, inplace=False)