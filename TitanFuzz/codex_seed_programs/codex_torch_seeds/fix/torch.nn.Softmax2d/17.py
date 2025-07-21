'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax2d\ntorch.nn.Softmax2d()\n'
import torch
import torch.nn as nn
input = torch.randn(1, 2, 3, 4)
print(input)
output = nn.Softmax2d()(input)
print(output)