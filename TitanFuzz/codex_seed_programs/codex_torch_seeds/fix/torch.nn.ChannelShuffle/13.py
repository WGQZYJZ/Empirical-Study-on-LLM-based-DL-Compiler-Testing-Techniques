'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ChannelShuffle\ntorch.nn.ChannelShuffle(groups)\n'
import torch
from torch.nn import ChannelShuffle
input_data = torch.Tensor(1, 16, 4, 4)
channel_shuffle = ChannelShuffle(groups=2)
output = channel_shuffle(input_data)
print(output)