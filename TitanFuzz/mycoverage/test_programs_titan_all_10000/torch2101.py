import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
torch.nn.init.ones_(input_tensor)
input_tensor = torch.randn(2, 3, 4)
torch.nn.init.ones_(input_tensor)