import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
torch.nn.init.constant_(input_tensor, 0.5)
input_tensor = torch.randn(2, 3)
torch.nn.init.eye_(input_tensor)