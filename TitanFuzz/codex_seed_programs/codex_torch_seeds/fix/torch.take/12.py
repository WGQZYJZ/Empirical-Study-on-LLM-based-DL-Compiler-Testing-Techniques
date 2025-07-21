'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.take\ntorch.take(input, index)\n'
import torch
input = torch.randn(3, 3)
print(input)
index = torch.tensor([0, 2, 1])
print(torch.take(input, index))