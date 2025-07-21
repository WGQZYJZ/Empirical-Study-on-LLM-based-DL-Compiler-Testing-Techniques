'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax2d\ntorch.nn.Softmax2d()\n'
import torch
import torch.nn as nn
input = torch.randn(2, 3, 3)
softmax = nn.Softmax2d()
output = softmax(input)
print(output)