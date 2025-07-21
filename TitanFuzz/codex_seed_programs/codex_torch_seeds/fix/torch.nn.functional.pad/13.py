"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
input = torch.randn(3, 3, 3)
output = torch.nn.functional.pad(input, (1, 1, 1, 1), mode='constant', value=0)
print(output)