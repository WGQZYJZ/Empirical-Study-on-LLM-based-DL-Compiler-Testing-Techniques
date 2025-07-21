import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 3)
torch.nn.init.ones_(input_tensor)