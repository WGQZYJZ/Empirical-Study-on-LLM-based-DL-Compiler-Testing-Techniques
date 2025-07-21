'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.take\ntorch.take(input, index)\n'
import torch
x = torch.arange(0, 9)
print(x)
index = torch.tensor([1, 2])
print(index)
print(torch.take(x, index))