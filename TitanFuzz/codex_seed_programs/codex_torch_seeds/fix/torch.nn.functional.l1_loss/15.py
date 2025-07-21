"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.l1_loss\ntorch.nn.functional.l1_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
import numpy as np
import torch
x = torch.tensor([[1, 2, 3], [1, 2, 3]], dtype=torch.float)
y = torch.tensor([[1, 2, 3], [1, 2, 3]], dtype=torch.float)
loss = torch.nn.functional.l1_loss(x, y)
print(loss)
loss = torch.nn.functional.l1_loss(x, y, reduction='sum')
print(loss)
loss = torch.nn.functional.l1_loss(x, y, reduction='none')
print(loss)