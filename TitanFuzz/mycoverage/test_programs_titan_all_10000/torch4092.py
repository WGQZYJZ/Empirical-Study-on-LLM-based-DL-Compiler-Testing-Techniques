import torch
from torch import nn
from torch.autograd import Variable
nonlinearity = 'relu'
param = None
gain = torch.nn.init.calculate_gain(nonlinearity, param)