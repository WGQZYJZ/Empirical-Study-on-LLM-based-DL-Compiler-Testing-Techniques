'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.row_stack\ntorch.row_stack(tensors, *, out=None)\n'
import torch
a = torch.rand(1, 3)
b = torch.rand(1, 3)
c = torch.rand(1, 3)
result = torch.row_stack([a, b, c])
print('result: ', result)