'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isreal\ntorch.isreal(input)\n'
import torch
x = torch.randn(3, 3)
y = torch.randn(3, 3)
z = torch.randn(3, 3)
print(torch.isreal(x))
print(torch.isreal(y))
print(torch.isreal(z))