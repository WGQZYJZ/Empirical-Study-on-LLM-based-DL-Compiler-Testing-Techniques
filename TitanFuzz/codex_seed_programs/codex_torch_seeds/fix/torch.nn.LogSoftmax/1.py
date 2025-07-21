'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch
x = torch.randn(1, requires_grad=True)
print('input data: ', x)
softmax = torch.nn.LogSoftmax(dim=0)
y = softmax(x)
print('output data: ', y)