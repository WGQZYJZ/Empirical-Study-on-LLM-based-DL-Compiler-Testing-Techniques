'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.constant_\ntorch.nn.init.constant_(tensor, val)\n'
import torch
input_tensor = torch.rand(4, 4)
print('Input tensor: {}'.format(input_tensor))
torch.nn.init.constant_(input_tensor, val=3.14)
print('Output tensor: {}'.format(input_tensor))