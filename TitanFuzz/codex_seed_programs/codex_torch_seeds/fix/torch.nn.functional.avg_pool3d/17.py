'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool3d\ntorch.nn.functional.avg_pool3d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
input_data = torch.arange(0, 27).view(1, 1, 3, 3, 3)
print(input_data)
output = torch.nn.functional.avg_pool3d(input_data, kernel_size=3, stride=1, padding=0)
print(output)