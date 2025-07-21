'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater_equal\ntorch.greater_equal(input, other, *, out=None)\n'
import torch
x = torch.tensor([1, 1, 1, 1, 1], dtype=torch.float32)
y = torch.tensor([1, 1, 1, 1, 1], dtype=torch.float32)
z = torch.greater_equal(x, y)
print(z)