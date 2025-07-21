'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax\ntorch.nn.Softmax(dim=None)\n'
import torch
x = torch.randn(2, 5)
print('Input data: \n', x)
softmax = torch.nn.Softmax(dim=1)
y = softmax(x)
print('Output data: \n', y)