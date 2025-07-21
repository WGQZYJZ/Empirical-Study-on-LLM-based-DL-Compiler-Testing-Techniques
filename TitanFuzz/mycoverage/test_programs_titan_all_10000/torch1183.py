import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(4, 4)
torch.distributed.Backend('gloo')