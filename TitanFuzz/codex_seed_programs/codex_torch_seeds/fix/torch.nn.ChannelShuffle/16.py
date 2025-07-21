'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ChannelShuffle\ntorch.nn.ChannelShuffle(groups)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 6, 2, 2))
channelShuffle = torch.nn.ChannelShuffle(3)
output = channelShuffle(input)
print('input:', input)
print('output:', output)