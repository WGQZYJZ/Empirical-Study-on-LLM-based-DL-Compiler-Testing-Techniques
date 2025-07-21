import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(3, 5))
torch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)
torch.nn.functional.feature_alpha_dropout(input, p=0.5, training=True, inplace=False)
torch.nn.functional.feature_alpha_dropout(input, p=0.5, training=True, inplace=True)