'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmax\ntorch.argmax(input, dim, keepdim=False)\n'
'\nTask 1: import PyTorch\n'
import torch
'\nTask 2: Generate input data\n'
input = torch.randn(3, 5)
print(input)
'\nTask 3: Call the API torch.argmax\ntorch.argmax(input, dim, keepdim=False)\n'
print(torch.argmax(input, 1))
print(torch.argmax(input, 1, keepdim=True))
print(torch.argmax(input, 0, keepdim=True))