'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log10\ntorch.log10(input, *, out=None)\n'
import torch
x = torch.arange(1, 11, dtype=torch.float)
print('The input data:\n', x)
y = torch.log10(x)
print('The result of torch.log10:', y)