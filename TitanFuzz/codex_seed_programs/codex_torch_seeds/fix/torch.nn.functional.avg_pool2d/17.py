'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool2d\ntorch.nn.functional.avg_pool2d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
input_data = torch.arange(1, 13, dtype=torch.float).reshape(1, 1, 4, 3)
output_data = F.avg_pool2d(input_data, kernel_size=2, stride=1, padding=0)
print('input_data:', input_data)
print('output_data:', output_data)