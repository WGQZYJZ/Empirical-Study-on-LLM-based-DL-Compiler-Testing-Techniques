'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sub\ntorch.sub(input, other, *, alpha=1, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
x = torch.rand(5, 3)
y = torch.rand(5, 3)
print('Task 3: Call the API torch.sub')
print(torch.sub(x, y))
print(x.sub(y))
print(torch.sub(x, 10))
print(x.sub(10))
print(torch.sub(10, x))