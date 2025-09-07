import torch
from torch import nn
from torch.autograd import Variable
data = torch.ones(2, 2)
torch.nn.init.constant_(data, val=3)