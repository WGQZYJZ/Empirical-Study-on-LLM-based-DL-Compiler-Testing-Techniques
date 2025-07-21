'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inner\ntorch.inner(input, other, *, out=None)\n'
import torch
print(torch.__version__)
input = torch.randn(4, 5)
other = torch.randn(5)
print(torch.inner(input, other))