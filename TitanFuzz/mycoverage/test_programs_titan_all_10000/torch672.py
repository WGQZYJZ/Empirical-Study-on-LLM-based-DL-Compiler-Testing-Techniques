import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4, 5)
output = torch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)