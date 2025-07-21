'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch
import torch.nn as nn
import torch
x = torch.randn(1, 3)
softmax = nn.LogSoftmax(dim=1)
y = softmax(x)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax\ntorch.nn.Softmax(dim=None)\n'
import torch
import torch.nn as nn
import torch
x = torch.randn(1, 3)
softmax = nn.Softmax(dim=1)
y = softmax(x)
print(y)