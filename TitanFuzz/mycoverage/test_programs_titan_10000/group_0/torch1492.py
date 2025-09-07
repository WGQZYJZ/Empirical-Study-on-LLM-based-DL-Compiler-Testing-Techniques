import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(3, 3)
torch.nn.init.eye_(input_tensor)