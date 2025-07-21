import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 3)
torch.clamp(x, min=0.2, max=0.8)