'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ChannelShuffle\ntorch.nn.ChannelShuffle(groups)\n'
import torch
import torch.nn as nn
import torch
input_data = torch.ones(1, 4, 4, 4)
layer = nn.ChannelShuffle(groups=2)
output = layer(input_data)
print(output)