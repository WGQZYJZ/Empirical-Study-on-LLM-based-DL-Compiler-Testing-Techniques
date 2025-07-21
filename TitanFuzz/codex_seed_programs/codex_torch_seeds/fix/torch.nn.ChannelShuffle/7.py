'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ChannelShuffle\ntorch.nn.ChannelShuffle(groups)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_tensor = torch.rand(2, 3, 4, 5)
channel_shuffle = nn.ChannelShuffle(groups=3)
output_tensor = channel_shuffle(input_tensor)
print(output_tensor)