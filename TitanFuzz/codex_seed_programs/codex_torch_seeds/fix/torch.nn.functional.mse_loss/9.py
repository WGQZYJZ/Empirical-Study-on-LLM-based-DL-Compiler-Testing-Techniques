"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.mse_loss\ntorch.nn.functional.mse_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
import torch
input = torch.randn(1, 1, 3, 3)
target = torch.randn(1, 1, 3, 3)
loss = nn.MSELoss()
output = loss(input, target)
print(output)
'\nExpected value:\ntensor(0.8656)\n'