'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
import torch.nn as nn
x = torch.randn(10, 5)
relu = nn.ReLU()
relu_x = relu(x)
print(relu_x)