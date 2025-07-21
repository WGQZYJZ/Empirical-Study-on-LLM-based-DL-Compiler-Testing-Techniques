import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
torch.clamp(input, min=0.5, max=1.5)