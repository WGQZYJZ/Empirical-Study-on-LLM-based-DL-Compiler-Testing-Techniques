import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3)
torch.nn.init.xavier_normal_(input_data, gain=1.0)