'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_storage\ntorch.is_storage(obj)\n'
import torch
x = torch.tensor([1, 2, 3])
y = torch.tensor([1, 2, 3])
z = (x + y)
print(z)
print(torch.is_storage(x))
print(torch.is_storage(y))
print(torch.is_storage(z))