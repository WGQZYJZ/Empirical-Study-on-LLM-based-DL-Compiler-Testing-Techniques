import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1)
torch.set_flush_denormal(True)
x = torch.randn(1)