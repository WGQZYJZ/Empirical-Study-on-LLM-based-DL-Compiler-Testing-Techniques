import torch
from torch import nn
from torch.autograd import Variable
nonlinearity = 'linear'
param = None
gain = torch.nn.init.calculate_gain(nonlinearity, param)
nonlinearity = 'relu'
param = None
gain = torch.nn.init.calculate_gain(nonlinearity, param)
nonlinearity = 'sigmoid'
param = None
gain = torch.nn.init.calculate_gain(nonlinearity, param)
nonlinearity = 'tanh'
param = None
gain = torch.nn.init.calculate_gain(nonlinearity, param)