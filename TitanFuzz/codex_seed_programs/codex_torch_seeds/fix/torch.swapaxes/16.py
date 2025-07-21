'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapaxes\ntorch.swapaxes(input, axis0, axis1)\n'
import torch
data = torch.randn(2, 3, 4)
print('data: ', data)
swap_data = torch.swapaxes(data, 0, 2)
print('swap_data: ', swap_data)