import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.ones(3, 5)
torch.nn.init.zeros_(input_data)