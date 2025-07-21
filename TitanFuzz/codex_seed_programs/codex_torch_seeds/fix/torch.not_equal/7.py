'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.not_equal\ntorch.not_equal(input, other, *, out=None)\n'
import torch
x = torch.tensor([[0, 1, 0], [1, 0, 1]])
y = torch.tensor([[0, 1, 0], [1, 1, 1]])
z = torch.not_equal(x, y)
print(z)
z = torch.not_equal(x, y, out=x)
print(z)