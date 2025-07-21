import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.rand(2, 2)
torch.nn.init.xavier_normal_(tensor, gain=1.0)