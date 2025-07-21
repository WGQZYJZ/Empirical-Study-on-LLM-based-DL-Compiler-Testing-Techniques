'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool3d\ntorch.nn.MaxPool3d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
input_data = torch.randn(1, 1, 5, 5, 5)
max_pool_3d = torch.nn.MaxPool3d(kernel_size=2, stride=1)
output = max_pool_3d(input_data)
print(output)
print(output.shape)