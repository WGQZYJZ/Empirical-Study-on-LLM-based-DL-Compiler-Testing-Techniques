import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 5)
torch.nn.init.xavier_uniform_(input_data)