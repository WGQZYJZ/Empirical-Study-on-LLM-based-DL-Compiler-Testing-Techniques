'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool2d\ntorch.nn.functional.adaptive_avg_pool2d(input, output_size)\n'
import torch
input = torch.randn(1, 1, 5, 5)
print('Input: ', input)
output = torch.nn.functional.adaptive_avg_pool2d(input, (2, 2))
print('Output: ', output)