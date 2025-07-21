'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('x = ', x)
k = 1
dim = 1
largest = True
sorted = True
y = torch.topk(x, k, dim, largest, sorted)
print('y = ', y)