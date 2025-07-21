'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool2d\ntorch.nn.functional.adaptive_avg_pool2d(input, output_size)\n'
import torch
import torch.nn.functional as F
input = torch.ones(1, 1, 3, 3)
print('Input is:', input)
output = F.adaptive_avg_pool2d(input, (2, 2))
print('Output is:', output)
'\nTask 4: Call the API torch.nn.functional.adaptive_max_pool2d\ntorch.nn.functional.adaptive_max_pool2d(input, output_size)\n'
import torch
import torch.nn.functional as F
input = torch.ones(1, 1, 3, 3)
print('Input is:', input)
output = F.adaptive_max_pool2d(input, (2, 2))
print('Output is:', output)
'\nTask 5: Call the API torch.nn.functional.avg_pool2d\ntorch.nn.functional.avg_pool2d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'