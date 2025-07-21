import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
torch.nn.init.constant_(input_tensor, val=3.14)