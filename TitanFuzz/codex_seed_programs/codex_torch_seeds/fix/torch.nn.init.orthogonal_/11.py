'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.orthogonal_\ntorch.nn.init.orthogonal_(tensor, gain=1)\n'
import torch
input = torch.randn(3, 3)
torch.nn.init.orthogonal_(input)
print('input after call the API: \n', input)