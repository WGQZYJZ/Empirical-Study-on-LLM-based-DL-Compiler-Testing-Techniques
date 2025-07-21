import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 4, 4, 4)
shuffle = torch.nn.ChannelShuffle(groups=2)
output = shuffle(input)