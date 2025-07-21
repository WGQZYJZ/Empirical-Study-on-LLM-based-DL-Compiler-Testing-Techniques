'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_default_dtype\ntorch.get_default_dtype()\n'
import torch
x = torch.tensor([1, 2, 3], dtype=torch.float32)
y = torch.tensor([2, 3, 4], dtype=torch.float32)
print(torch.get_default_dtype())
print(x.dtype)
print(y.dtype)
print(torch.add(x, y))
print(torch.add(x, y).dtype)
print((torch.add(x, y).dtype == torch.float32))
print((torch.add(x, y).dtype == torch.float64))
print(torch.tensor(1, dtype=torch.float32).dtype)
print(torch.tensor(1, dtype=torch.float64).dtype)