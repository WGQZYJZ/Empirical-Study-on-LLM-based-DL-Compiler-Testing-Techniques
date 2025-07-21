'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.orthogonal_\ntorch.nn.init.orthogonal_(tensor, gain=1)\n'
import torch
tensor = torch.randn(2, 3)
print('Input tensor: ', tensor)
torch.nn.init.orthogonal_(tensor)
print('Output tensor: ', tensor)