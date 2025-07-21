'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch
input = torch.randn(2, 3)
print('Input:')
print(input)
output = torch.nn.LogSoftmax(dim=1)(input)
print('Output:')
print(output)