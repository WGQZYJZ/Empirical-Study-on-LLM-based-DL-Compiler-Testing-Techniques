import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 5)
torch.nn.init.xavier_normal_(input_tensor)