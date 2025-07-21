'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ChannelShuffle\ntorch.nn.ChannelShuffle(groups)\n'
import torch
import torch
input = torch.randn(1, 4, 4, 4)
print('Input shape: ', input.shape)
shuffle = torch.nn.ChannelShuffle(groups=2)
output = shuffle(input)
print('Output shape: ', output.shape)