'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
input = torch.randn(1, 2, 5, 5)
avg_pool2d = torch.nn.AdaptiveAvgPool2d(output_size=(2, 2))
output = avg_pool2d(input)
print('Input size: {}'.format(input.size()))
print('Output size: {}'.format(output.size()))