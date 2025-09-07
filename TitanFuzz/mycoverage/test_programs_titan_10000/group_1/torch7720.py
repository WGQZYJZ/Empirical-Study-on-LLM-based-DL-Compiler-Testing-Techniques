import torch
from torch import nn
from torch.autograd import Variable

inp = torch.randn(1, 2, 3)
relu = torch.nn.SiLU(inplace=False)