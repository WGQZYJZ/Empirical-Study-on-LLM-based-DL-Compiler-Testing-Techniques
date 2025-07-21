import torch
from torch import nn
from torch.autograd import Variable
nonlinearity = 'linear'
param = None
gain = torch.nn.init.calculate_gain(nonlinearity, param)