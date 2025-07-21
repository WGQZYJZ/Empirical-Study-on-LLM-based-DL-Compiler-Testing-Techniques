"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
input = torch.randn(1, 3, 5, 5)
pad = (2, 3, 3, 2)
print(input)
print(torch.nn.functional.pad(input, pad, mode='constant', value=0))