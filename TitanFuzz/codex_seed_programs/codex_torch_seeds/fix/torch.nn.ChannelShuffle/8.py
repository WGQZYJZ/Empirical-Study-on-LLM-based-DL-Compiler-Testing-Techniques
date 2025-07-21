'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ChannelShuffle\ntorch.nn.ChannelShuffle(groups)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 4, 4, 4)
shuffle = nn.ChannelShuffle(2)
output = shuffle(input_data)
print(output)