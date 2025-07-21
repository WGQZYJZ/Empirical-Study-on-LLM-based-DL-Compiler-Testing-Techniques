'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
import torch.nn.functional as F
x = torch.randn(2, 3)
print(x)
print(F.dropout(x, training=True))
print(F.dropout(x, training=False))