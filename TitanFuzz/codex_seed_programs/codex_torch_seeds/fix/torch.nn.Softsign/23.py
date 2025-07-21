'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
import torch.nn as nn
import torch
x = torch.randn(1, 1, 2, 2)
softsign = nn.Softsign()
print(softsign(x))