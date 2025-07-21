import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 4)
torch.nn.init.zeros_(input_data)