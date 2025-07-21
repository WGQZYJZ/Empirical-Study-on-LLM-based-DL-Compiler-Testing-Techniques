'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multiply\ntorch.multiply(input, other, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
y = torch.tensor([2, 2, 2, 2], dtype=torch.float32)
z = torch.multiply(x, y)
print(z)
z = torch.div(x, y)
print(z)
z = torch.pow(x, y)
print(z)
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
y = torch.tensor([[2, 2], [2, 2]], dtype=torch.float32)
z = torch.mm(x, y)
print(z)