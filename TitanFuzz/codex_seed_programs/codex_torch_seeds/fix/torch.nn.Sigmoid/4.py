'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sigmoid\ntorch.nn.Sigmoid()\n'
import torch
import torch.nn as nn
x = torch.tensor([1, 2, 3, 4, 5])
sigmoid = nn.Sigmoid()
print(sigmoid(x))