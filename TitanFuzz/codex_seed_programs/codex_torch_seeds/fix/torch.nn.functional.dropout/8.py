'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
x = torch.randn(1, 10)
y = F.dropout(x, p=0.5, training=True, inplace=False)
print(y)
print(y.shape)
print(y.type())
print(y)
y = F.dropout(x, p=0.5, training=False, inplace=False)
print(y)
y = F.dropout(x, p=0.5, training=True, inplace=False)
print(y)