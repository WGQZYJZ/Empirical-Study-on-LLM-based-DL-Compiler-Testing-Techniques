import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
torch.nn.init.zeros_(input_tensor)