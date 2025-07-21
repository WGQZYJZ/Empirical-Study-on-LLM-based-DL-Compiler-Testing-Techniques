import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.ones(5, 5)
torch.nn.init.eye_(input_data)