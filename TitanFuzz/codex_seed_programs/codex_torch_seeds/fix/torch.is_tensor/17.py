'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_tensor\ntorch.is_tensor(obj)\n'
import torch
x = torch.randn(2, 3)
y = torch.ones(2, 3)
z = torch.ones(2, 3)
print(torch.is_tensor(x))
print(torch.is_tensor(y))
print(torch.is_tensor(z))