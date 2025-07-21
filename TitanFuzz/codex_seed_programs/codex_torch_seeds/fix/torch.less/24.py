'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
print(torch.__version__)
x = torch.rand(5, 3)
y = torch.rand(5, 3)
print(torch.less(x, y))