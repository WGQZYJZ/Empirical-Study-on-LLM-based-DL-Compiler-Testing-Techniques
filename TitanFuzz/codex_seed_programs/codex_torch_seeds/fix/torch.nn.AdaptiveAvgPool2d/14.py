'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
import torch.nn as nn
print('Task 1')
print('PyTorch version: ', torch.__version__)
print('\nTask 2')
print('Generate input data')
input = torch.randn(1, 3, 5, 5)
print('Input size: ', input.size())
print('\nTask 3')
print('Call the API torch.nn.AdaptiveAvgPool2d')
print('torch.nn.AdaptiveAvgPool2d(output_size)')
print('output_size = (1, 1)')
avgpool2d = nn.AdaptiveAvgPool2d(output_size=(1, 1))
output = avgpool2d(input)
print('Output size: ', output.size())
print('Output: ', output)