'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapaxes\ntorch.swapaxes(input, axis0, axis1)\n'
import torch
input = torch.randn(2, 3, 5)
print(input)
swap_input = torch.swapaxes(input, 0, 1)
print(swap_input)