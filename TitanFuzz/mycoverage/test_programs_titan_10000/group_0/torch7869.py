import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(2, 3, 4)
torch.nn.SiLU(inplace=False)(x)
x = torch.randn(2, 3, 4)
torch.nn.Softplus(beta=1, threshold=20)(x)