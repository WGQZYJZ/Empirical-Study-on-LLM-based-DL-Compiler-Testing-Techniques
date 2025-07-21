import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.ones(2, 2)
torch.nn.init.constant_(input_data, 2)
input_data = torch.empty(2, 2)
torch.nn.init.ones_(input_data)
input_data = torch.empty(2, 2)
torch.nn.init.zeros_(input_data)