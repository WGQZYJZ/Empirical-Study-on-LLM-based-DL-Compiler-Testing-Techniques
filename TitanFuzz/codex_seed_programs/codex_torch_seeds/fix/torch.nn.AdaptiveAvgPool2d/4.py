'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
input = torch.randn(1, 1, 10, 10)
output = torch.nn.AdaptiveAvgPool2d(output_size=5)(input)
print('input: ', input)
print('output: ', output)