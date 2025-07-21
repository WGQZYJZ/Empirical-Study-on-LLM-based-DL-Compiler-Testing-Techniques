import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
torch.nn.init.ones_(input_data)
input_data = torch.randn(2, 3)
torch.nn.init.zeros_(input_data)
input_data = torch.randn(2, 3)