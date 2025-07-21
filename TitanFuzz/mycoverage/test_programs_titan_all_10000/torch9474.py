import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4, 5)
output = torch.nn.functional.alpha_dropout(input, p=0.5, training=False, inplace=False)