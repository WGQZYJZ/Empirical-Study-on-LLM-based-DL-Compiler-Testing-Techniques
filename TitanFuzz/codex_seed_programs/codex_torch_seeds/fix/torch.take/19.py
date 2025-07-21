'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.take\ntorch.take(input, index)\n'
import torch
input = torch.randn(3, 5)
index = torch.tensor([0, 3])
print(input)
print(index)
print(torch.take(input, index))