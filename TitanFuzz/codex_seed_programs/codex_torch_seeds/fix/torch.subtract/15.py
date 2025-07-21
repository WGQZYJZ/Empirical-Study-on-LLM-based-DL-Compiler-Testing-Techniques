'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.subtract\ntorch.subtract(input, other, *, alpha=1, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
y = torch.tensor([[1, 1, 1], [1, 1, 1]], dtype=torch.float32)
z = torch.subtract(x, y)
print(z)