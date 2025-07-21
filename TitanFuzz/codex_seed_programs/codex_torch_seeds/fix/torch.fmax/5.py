'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[7, 8, 9], [10, 11, 12]])
z = torch.fmax(x, y)
print(z)