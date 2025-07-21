'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.constant_\ntorch.nn.init.constant_(tensor, val)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: \n', input_tensor)
torch.nn.init.constant_(input_tensor, val=5)
print('Output tensor: \n', input_tensor)