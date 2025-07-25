'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch._assert\ntorch._assert(condition, message)\n'
import torch
a = torch.randn(1, requires_grad=True)
print(a)
b = torch.randn(1, requires_grad=True)
print(b)
c = (a + b)
print(c)
d = c.sum()
print(d)
torch._assert(d.requires_grad, 'd must require grad')
print(('-' * 50))
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch._assert')
print('torch._assert(condition, message)')