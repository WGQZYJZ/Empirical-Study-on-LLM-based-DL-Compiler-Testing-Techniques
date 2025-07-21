'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_conj\ntorch.is_conj(input)\n'
import torch
input = torch.randn(4, 4)
output = torch.is_conj(input)
print(input)
print(output)