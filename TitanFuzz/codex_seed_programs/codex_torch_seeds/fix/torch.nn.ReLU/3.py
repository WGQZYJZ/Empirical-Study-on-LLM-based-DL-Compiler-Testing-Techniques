'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
x = torch.randn(2, 3)
print(x)
relu = torch.nn.ReLU()
print(relu(x))