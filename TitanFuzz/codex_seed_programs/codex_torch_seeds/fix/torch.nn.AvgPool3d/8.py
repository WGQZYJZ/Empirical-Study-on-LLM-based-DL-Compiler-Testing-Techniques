'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool3d\ntorch.nn.AvgPool3d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
from torch.nn import AvgPool3d
input_data = torch.randn(20, 16, 50, 32, 32)
pooling = AvgPool3d(kernel_size=(2, 2, 2))
output = pooling(input_data)
print(output.size())