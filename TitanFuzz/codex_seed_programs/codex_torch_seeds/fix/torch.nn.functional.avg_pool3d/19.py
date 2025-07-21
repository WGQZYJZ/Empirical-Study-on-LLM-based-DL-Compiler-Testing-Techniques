'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool3d\ntorch.nn.functional.avg_pool3d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch.nn.functional as F
input_data = torch.randn(1, 1, 4, 4, 4)
print(input_data)
output = F.avg_pool3d(input_data, kernel_size=2, stride=2)
print(output)