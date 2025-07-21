'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmax\ntorch.argmax(input, dim, keepdim=False)\n'
import torch
input = torch.randn(2, 3)
print(input)
index = torch.argmax(input, dim=1)
print(index)
index = torch.argmax(input, dim=1, keepdim=True)
print(index)