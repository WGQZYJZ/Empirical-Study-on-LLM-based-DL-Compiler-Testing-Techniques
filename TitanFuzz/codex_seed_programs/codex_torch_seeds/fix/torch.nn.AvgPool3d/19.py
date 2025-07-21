'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool3d\ntorch.nn.AvgPool3d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
input = torch.randn(20, 16, 50, 32, 32)
print(input.size())
output = torch.nn.AvgPool3d(kernel_size=(2, 2, 2))(input)
print(output.size())
'\nTask 4: Call the API torch.nn.MaxPool3d\ntorch.nn.MaxPool3d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
input = torch.randn(20, 16, 50, 32, 32)
print(input.size())
output = torch.nn.MaxPool3d(kernel_size=(2, 2, 2))(input)
print(output.size())
'\nTask 5: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
input = torch.randn(20, 16, 50, 32, 32)
print(input.size())
output