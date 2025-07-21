'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.subtract\ntorch.subtract(input, other, *, alpha=1, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([1, 1, 1, 1, 1])
print('Task 3: Call the API torch.subtract')
z = torch.subtract(x, y)
print('The result of torch.subtract(x, y) is: ', z)