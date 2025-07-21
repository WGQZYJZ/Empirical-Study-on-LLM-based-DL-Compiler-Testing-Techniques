'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool3d\ntorch.nn.functional.avg_pool3d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
input_data = torch.rand(4, 16, 32, 32, 32)
avg_pool3d_output = torch.nn.functional.avg_pool3d(input_data, kernel_size=3, stride=1, padding=1)
print(avg_pool3d_output.shape)