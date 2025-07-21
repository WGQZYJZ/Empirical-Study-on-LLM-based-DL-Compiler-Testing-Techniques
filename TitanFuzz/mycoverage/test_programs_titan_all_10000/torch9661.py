import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.rand(2, 3)
torch.nn.init.constant_(tensor, val=0.5)