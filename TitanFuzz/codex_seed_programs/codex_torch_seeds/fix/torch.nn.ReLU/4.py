'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
x = torch.randn(1, 3)
print(x)
y = torch.nn.ReLU()
print(y(x))
y = torch.nn.ReLU(inplace=True)
print(y(x))
print(x)