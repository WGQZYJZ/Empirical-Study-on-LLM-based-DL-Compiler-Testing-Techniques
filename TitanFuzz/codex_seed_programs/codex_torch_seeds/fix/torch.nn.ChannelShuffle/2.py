'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ChannelShuffle\ntorch.nn.ChannelShuffle(groups)\n'
import torch
import torch
input = torch.randn(2, 4, 2, 2)
out = torch.nn.ChannelShuffle(2)(input)
print(out)