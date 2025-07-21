import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, 3)
output = torch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)