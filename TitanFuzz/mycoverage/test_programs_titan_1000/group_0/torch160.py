import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 16)
input
torch.nn.functional.alpha_dropout(input, p=0.5, training=False, inplace=False)
torch.nn.functional.alpha_dropout(input, p=0.5, training=True, inplace=False)
torch.nn.functional.alpha_dropout(input, p=0.5, training=True, inplace=True)
input
input = torch.randn(20, 16)
input
torch.nn.functional.dropout(input, p=0.5, training=False, inplace=False)