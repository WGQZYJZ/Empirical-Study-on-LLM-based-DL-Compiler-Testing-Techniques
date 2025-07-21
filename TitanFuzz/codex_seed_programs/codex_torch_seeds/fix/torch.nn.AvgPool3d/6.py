'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool3d\ntorch.nn.AvgPool3d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch
input = torch.randn(20, 16, 50, 32, 45)
output = torch.nn.AvgPool3d(kernel_size=3, stride=2, padding=1)(input)
print(output.size())