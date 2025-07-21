'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LocalResponseNorm\ntorch.nn.LocalResponseNorm(size, alpha=0.0001, beta=0.75, k=1.0)\n'
import torch
input_data = torch.randn(1, 1, 5, 5)
print(input_data)
import torch
input_data = torch.randn(1, 1, 5, 5)
norm_data = torch.nn.LocalResponseNorm(size=2, alpha=0.0001, beta=0.75, k=1.0)
output = norm_data(input_data)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool1d\ntorch.nn.MaxPool1d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
input_data = torch.randn(1, 1, 5, 5)
print(input_data)
import torch
input_data = torch.randn(1, 1, 5, 5)