'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool1d\ntorch.nn.functional.avg_pool1d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
import torch.nn.functional as F
input_data = torch.randn(1, 1, 4)
output_data = F.avg_pool1d(input_data, kernel_size=2)
print(output_data)