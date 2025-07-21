'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.constant_\ntorch.nn.init.constant_(tensor, val)\n'
import torch
tensor = torch.zeros(2, 3)
print('Input tensor: ', tensor)
torch.nn.init.constant_(tensor, 3.14)
print('Output tensor: ', tensor)