'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
x = torch.randn(3, 3)
print(x)
relu = torch.nn.ReLU()
y = relu(x)
print(y)