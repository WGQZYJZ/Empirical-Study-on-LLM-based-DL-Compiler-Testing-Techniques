'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logaddexp\ntorch.logaddexp(input, other, *, out=None)\n'
import torch
data1 = torch.randn(3, 4)
data2 = torch.randn(3, 4)
print(torch.logaddexp(data1, data2))