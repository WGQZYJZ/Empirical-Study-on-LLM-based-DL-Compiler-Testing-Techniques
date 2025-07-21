'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_tensor\ntorch.is_tensor(obj)\n'
import torch
x = torch.rand(3, 3)
y = torch.rand(3, 3)
z = (x + y)
print(z)
print(torch.is_tensor(x))
print(torch.is_tensor(y))
print(torch.is_tensor(z))