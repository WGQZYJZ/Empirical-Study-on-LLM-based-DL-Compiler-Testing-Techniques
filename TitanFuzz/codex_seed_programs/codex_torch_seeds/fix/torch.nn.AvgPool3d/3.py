'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool3d\ntorch.nn.AvgPool3d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch
input_data = torch.randn(4, 16, 5, 5, 5)
avg_pool3d = torch.nn.AvgPool3d(kernel_size=3, stride=2, padding=1)
output = avg_pool3d(input_data)
print(output.shape)