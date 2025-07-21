'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sub\ntorch.sub(input, other, *, alpha=1, out=None)\n'
import torch
import torch
x = torch.randn(4, 4)
y = torch.randn(4, 4)
z = torch.sub(x, y)
print(z)