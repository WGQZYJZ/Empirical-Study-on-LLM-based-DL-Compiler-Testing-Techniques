'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool3d\ntorch.nn.functional.max_pool3d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn.functional as F
import torch
batch_size = 2
in_channels = 3
in_depth = 5
in_height = 8
in_width = 8
input = torch.randn(batch_size, in_channels, in_depth, in_height, in_width)
print(input.shape)
output = F.max_pool3d(input, kernel_size=2, stride=2)
print(output.shape)