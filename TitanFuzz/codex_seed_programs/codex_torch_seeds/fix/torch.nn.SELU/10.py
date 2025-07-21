'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
import torch.nn as nn
import torch
x = torch.randn(10)
selu_layer = nn.SELU(inplace=False)
print(selu_layer(x))