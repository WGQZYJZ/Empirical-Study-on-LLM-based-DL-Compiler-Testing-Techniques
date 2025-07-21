'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.log_softmax\ntorch.special.log_softmax(input, dim, *, dtype=None)\n'
import torch
input = torch.randn(1, 3)
print('Input: ', input)
output = torch.special.log_softmax(input, dim=0)
print('Output: ', output)
'\nTask 4: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch.nn as nn
output = nn.LogSoftmax(dim=0)(input)
print('Output: ', output)