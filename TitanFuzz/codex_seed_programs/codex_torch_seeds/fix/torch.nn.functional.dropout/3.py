'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
x = torch.randn(2, 3, requires_grad=True)
y = F.dropout(x, p=0.5, training=True)
print(x)
print(y)