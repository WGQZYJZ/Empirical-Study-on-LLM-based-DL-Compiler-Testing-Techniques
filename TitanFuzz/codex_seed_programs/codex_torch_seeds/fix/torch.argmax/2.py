'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmax\ntorch.argmax(input, dim, keepdim=False)\n'
import torch
input = torch.rand(2, 3, 5)
print(input)
print(torch.argmax(input, dim=0))
print(torch.argmax(input, dim=1))
print(torch.argmax(input, dim=2))