import torch
from torch import nn
from torch.autograd import Variable
tensor_x = torch.randn(2, 3)
tensor_clamp = torch.clamp(tensor_x, min=(- 0.5), max=0.5)