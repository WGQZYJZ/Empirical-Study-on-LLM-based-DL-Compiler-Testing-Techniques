'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
a = torch.rand(3, 4)
b = torch.rand(3, 4)
c = torch.column_stack((a, b))
print(c)
'\nTask 4: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
c = torch.column_stack((a, b), out=torch.FloatTensor(3, 8))
print(c)