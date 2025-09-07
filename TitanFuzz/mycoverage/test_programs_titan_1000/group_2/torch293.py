import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
torch.nn.init.xavier_normal_(input_data)
input_data = torch.randn(2, 3)
torch.nn.init.xavier_uniform_(input_data)