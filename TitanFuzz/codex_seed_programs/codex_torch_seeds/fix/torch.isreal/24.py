'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isreal\ntorch.isreal(input)\n'
import torch
x = torch.randn(2, 3)
print(x)
print(torch.isreal(x))
x = torch.randn(2, 3, dtype=torch.complex64)
print(x)
print(torch.isreal(x))