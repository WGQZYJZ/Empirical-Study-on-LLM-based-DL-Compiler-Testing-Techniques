'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapaxes\ntorch.swapaxes(input, axis0, axis1)\n'
import torch
data = torch.arange(0, 6).reshape((2, 3))
print('data:', data)
print('torch.swapaxes(data, 0, 1):', torch.swapaxes(data, 0, 1))