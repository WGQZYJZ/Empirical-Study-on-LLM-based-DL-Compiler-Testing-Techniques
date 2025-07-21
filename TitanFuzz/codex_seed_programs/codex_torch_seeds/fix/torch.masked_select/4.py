'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.masked_select\ntorch.masked_select(input, mask, *, out=None)\n'
import torch
x = torch.randn(3, 4)
mask = torch.ByteTensor([[0, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 1]])
y = torch.masked_select(x, mask)
print(y)
z = torch.masked_select(x, mask, out=torch.empty(2, dtype=torch.float))
print(z)