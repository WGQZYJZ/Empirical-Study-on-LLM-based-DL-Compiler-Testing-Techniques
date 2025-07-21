import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 1, 3, 3)
torch.nn.AlphaDropout(p=0.5, inplace=False)