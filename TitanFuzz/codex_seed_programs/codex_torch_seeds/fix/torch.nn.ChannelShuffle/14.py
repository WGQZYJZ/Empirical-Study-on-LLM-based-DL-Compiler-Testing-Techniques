'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ChannelShuffle\ntorch.nn.ChannelShuffle(groups)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.randn(1, 3, 5, 5)
channel_shuffle = nn.ChannelShuffle(3)
output_data = channel_shuffle(input_data)
print(output_data)