'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ChannelShuffle\ntorch.nn.ChannelShuffle(groups)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(1, 2, 4, 4)
channel_shuffle = nn.ChannelShuffle(2)
output = channel_shuffle(input)
print(output)