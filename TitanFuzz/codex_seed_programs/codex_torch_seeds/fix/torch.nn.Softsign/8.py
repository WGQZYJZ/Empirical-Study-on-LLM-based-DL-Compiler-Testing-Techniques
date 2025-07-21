'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
import torch.nn as nn
data = torch.randn(2, 2)
print(data)
softsign = nn.Softsign()
print(softsign(data))