'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ChannelShuffle\ntorch.nn.ChannelShuffle(groups)\n'
import torch
from torch.nn import ChannelShuffle
import torch
input_data = torch.randn(1, 4, 2, 2)
channel_shuffle = ChannelShuffle(2)
output = channel_shuffle(input_data)
print(output)