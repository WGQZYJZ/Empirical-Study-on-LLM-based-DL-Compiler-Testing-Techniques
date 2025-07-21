import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
torch.nn.init.constant_(input_data, val=0.5)