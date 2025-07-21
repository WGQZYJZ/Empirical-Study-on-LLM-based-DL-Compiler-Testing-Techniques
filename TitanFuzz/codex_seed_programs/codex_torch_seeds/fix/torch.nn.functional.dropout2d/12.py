'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout2d\ntorch.nn.functional.dropout2d(input, p=0.5, training=True, inplace=False)\n'
import torch
import torch.nn.functional as F
import torch
x = torch.randn(1, 1, 4, 4)
y = F.dropout2d(x, p=0.5, training=True, inplace=False)
print('Input data:')
print(x)
print('Dropout result:')
print(y)