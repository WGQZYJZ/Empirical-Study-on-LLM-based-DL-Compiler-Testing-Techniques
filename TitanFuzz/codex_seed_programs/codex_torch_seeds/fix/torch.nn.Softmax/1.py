'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax\ntorch.nn.Softmax(dim=None)\n'
import torch
import torch.nn as nn
x = torch.randn(2, 3)
print(x)
softmax = nn.Softmax(dim=1)
y = softmax(x)
print(y)
print(torch.sum(y, dim=1))
'\nTask 4: Call the API torch.nn.Softmax2d\ntorch.nn.Softmax2d(dim=None)\n'
softmax2d = nn.Softmax2d()
x = torch.randn(2, 3, 4)
print(x)
y = softmax2d(x)
print(y)
print(torch.sum(y, dim=1))
'\nTask 5: Call the API torch.nn.Softmax2d\ntorch.nn.LogSoftmax(dim=None)\n'
log_softmax = nn.LogSoftmax(dim=1)
x = torch.randn(2, 3)
print(x)
y = log_softmax(x)