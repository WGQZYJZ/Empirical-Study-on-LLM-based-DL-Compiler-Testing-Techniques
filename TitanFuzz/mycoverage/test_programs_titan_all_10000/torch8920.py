import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 6, 2, 2))
channelShuffle = torch.nn.ChannelShuffle(3)
output = channelShuffle(input)