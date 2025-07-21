"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
input = torch.randn(1, 3, 3, 3)
print(input)
pad = (1, 1, 1, 1)
print(torch.nn.functional.pad(input, pad, mode='constant', value=0))
pad = (1, 1, 1, 1, 2, 2, 2, 2)
print(torch.nn.functional.pad(input, pad, mode='constant', value=0))