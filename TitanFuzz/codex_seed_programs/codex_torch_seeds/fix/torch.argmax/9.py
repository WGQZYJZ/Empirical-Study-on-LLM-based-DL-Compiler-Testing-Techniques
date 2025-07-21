'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmax\ntorch.argmax(input, dim, keepdim=False)\n'
import torch
x = torch.randn(2, 3)
print(x)
print(torch.argmax(x, dim=1))
print(torch.argmax(x, dim=1, keepdim=True))
print(torch.argmax(x, dim=0, keepdim=True))
print(torch.argmax(x, dim=(- 1), keepdim=True))