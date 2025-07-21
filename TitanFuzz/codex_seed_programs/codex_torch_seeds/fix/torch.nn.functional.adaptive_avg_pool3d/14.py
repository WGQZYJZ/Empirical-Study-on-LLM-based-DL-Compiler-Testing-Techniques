'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool3d\ntorch.nn.functional.adaptive_avg_pool3d(input, output_size)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
input_data = torch.rand(1, 2, 4, 5, 6)
output = F.adaptive_avg_pool3d(input_data, (1, 1, 1))
print('input_data: ', input_data)
print('output: ', output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool3d\ntorch.nn.functional.avg_pool3d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F