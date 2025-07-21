'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multiply\ntorch.multiply(input, other, *, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(torch.multiply(x, y))
print((x * y))