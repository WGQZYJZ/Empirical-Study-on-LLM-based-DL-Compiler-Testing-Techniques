'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.take\ntorch.take(input, index)\n'
import torch
input = torch.randn(4, 4)
index = torch.tensor([0, 2])
output = torch.take(input, index)
print(input)
print(output)