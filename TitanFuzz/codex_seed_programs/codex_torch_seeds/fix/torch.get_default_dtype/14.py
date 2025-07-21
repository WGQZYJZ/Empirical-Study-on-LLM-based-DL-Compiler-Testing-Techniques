'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_default_dtype\ntorch.get_default_dtype()\n'
import torch
x = torch.tensor([1, 2, 3])
print(x)
y = torch.tensor([1.0, 2.0, 3.0])
print(y)
z = torch.tensor([1, 2, 3], dtype=torch.float64)
print(z)
print(torch.get_default_dtype())