'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
x = torch.randn(4)
y = torch.randn(4)
z = torch.empty(4)
torch.lerp(x, y, 0.5, out=z)
print(z)