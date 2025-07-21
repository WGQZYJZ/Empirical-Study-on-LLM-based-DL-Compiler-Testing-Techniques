'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxUnpool2d\ntorch.nn.MaxUnpool2d(kernel_size, stride=None, padding=0)\n'
import torch
import torch.nn as nn
input_data = torch.rand(1, 1, 3, 3)
indices = torch.tensor([[[[0, 0, 0], [0, 0, 0], [0, 0, 0]]]])
max_unpool2d = nn.MaxUnpool2d(kernel_size=2, stride=2)
output_data = max_unpool2d(input_data, indices)
print(output_data)