import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4)
torch.nn.init.dirac_(input_data)