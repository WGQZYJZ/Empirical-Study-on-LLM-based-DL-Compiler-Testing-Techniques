import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(2, 3))
torch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)
input = Variable(torch.randn(2, 3))