'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
import torch.nn.functional as F
import torch
x = torch.tensor([[1, 2, 3], [1, 2, 3], [1, 2, 3]], dtype=torch.float)
y = F.dropout(x, p=0.5, training=True)
print(y)
y = F.dropout(x, p=0.5, training=False)
print(y)
y = F.dropout(x, p=0.5, training=True, inplace=True)
print(y)