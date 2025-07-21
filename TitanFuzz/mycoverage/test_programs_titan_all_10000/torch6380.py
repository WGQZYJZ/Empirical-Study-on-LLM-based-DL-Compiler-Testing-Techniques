import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
torch.nn.init.normal_(input_data)
input_data = torch.randn(2, 3)
torch.nn.init.normal_(input_data, mean=0.5, std=0.5)
input_data = torch.randn(2, 3)
torch.nn.init.normal_(input_data, mean=0.5, std=0.5)