'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmax\ntorch.argmax(input, dim, keepdim=False)\n'
import torch
import torch
input = torch.randn(3, 5)
print(input)
index = torch.argmax(input, dim=1)
print(index)