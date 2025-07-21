'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
import torch.nn.functional as F
import torch
x = torch.ones(2, 2)
print(x)
y = F.dropout(x, p=0.5, training=True)
print(y)