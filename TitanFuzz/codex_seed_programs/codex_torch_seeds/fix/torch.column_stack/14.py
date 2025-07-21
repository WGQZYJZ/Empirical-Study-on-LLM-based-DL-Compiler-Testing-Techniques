'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
a = torch.randn(3, 4)
b = torch.randn(3, 4)
print('Input tensor a:', a)
print('Input tensor b:', b)
c = torch.column_stack((a, b))
print('Output tensor c:', c)