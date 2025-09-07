import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
torch.nn.init.kaiming_normal_(input_data, mode='fan_in', nonlinearity='leaky_relu')