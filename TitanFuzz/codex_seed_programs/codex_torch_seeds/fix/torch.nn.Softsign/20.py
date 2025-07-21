'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
x = torch.randn(1, 3)
print(x)
y = torch.nn.Softsign()
print(y(x))