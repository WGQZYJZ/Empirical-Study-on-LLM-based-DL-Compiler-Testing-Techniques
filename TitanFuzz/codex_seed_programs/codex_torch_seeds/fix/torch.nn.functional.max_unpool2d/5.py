'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_unpool2d\ntorch.nn.functional.max_unpool2d(input, indices, kernel_size, stride=None, padding=0, output_size=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(1, 1, 4, 4)
indices = torch.tensor([[[[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1]]]])
output = F.max_unpool2d(input, indices, 2)
print(output)