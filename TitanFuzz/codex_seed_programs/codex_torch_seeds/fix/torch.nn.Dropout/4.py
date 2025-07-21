'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
x = torch.randn(100, 1000)
y = torch.nn.Dropout(p=0.5, inplace=False)(x)
print(x[0, :10])
print(y[0, :10])