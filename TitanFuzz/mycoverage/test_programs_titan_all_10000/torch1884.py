import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 5)
torch.nn.init.constant_(input_data, val=0.0)