'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool1d\ntorch.nn.functional.avg_pool1d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
import torch
input_data = torch.randn(1, 1, 5)
output = torch.nn.functional.avg_pool1d(input_data, kernel_size=3, stride=2, padding=1)
print('input_data: {}'.format(input_data))
print('output: {}'.format(output))