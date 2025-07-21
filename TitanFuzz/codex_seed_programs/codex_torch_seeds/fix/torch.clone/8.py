'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clone\ntorch.clone(input, *, memory_format=torch.preserve_format)\n'
import torch
input = torch.rand(3, 5)
output = torch.clone(input)
print(output)