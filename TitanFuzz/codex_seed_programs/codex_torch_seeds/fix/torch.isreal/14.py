'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isreal\ntorch.isreal(input)\n'
import torch
x = torch.randn(1, 2, 3)
y = torch.randn(1, 2, 3)
print(x)
print(y)
print(torch.isreal(x))
print(torch.isreal(y))
print(torch.isreal((x + y)))
print(torch.isreal((x + (1j * y))))