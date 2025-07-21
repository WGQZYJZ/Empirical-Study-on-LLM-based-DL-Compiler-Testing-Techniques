'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.real\ntorch.real(input)\n'
import torch
x = torch.randn(4, 4)
y = torch.randn(4, 4)
print(x)
print(y)
print(torch.real(x))
print(torch.real(y))