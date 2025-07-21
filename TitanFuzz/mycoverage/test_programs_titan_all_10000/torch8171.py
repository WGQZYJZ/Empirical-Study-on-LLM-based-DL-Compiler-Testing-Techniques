import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.ones(2, 2)
torch.nn.init.ones_(input_data)