'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erfinv\ntorch.erfinv(input, *, out=None)\n'
import torch
x = torch.rand(1, requires_grad=True)
y = torch.erfinv(x)
print('The input is:', x)
print('The output is:', y)