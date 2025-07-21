'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxUnpool1d\ntorch.nn.MaxUnpool1d(kernel_size, stride=None, padding=0)\n'
import torch
import torch.nn as nn
input = torch.tensor([[[2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]], dtype=torch.float)
indices = torch.tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]], dtype=torch.long)
max_unpool1d = nn.MaxUnpool1d(kernel_size=2, stride=2, padding=0)
output = max_unpool1d(input, indices)
print(output)