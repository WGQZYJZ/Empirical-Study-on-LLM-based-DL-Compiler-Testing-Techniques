'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout2d\ntorch.nn.functional.dropout2d(input, p=0.5, training=True, inplace=False)\n'
import torch
import torch.nn.functional as F
x = torch.randn(1, 1, 10, 10)
print('x: ', x)
y = F.dropout2d(x, 0.5, training=True)
print('y: ', y)
y = F.dropout2d(x, 0.5, training=False)
print('y: ', y)