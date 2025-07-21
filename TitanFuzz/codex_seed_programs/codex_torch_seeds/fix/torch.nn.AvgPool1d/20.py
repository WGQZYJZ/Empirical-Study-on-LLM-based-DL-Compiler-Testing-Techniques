'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool1d\ntorch.nn.AvgPool1d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
import torch.nn as nn
input_data = torch.tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]], dtype=torch.float32)
avgpool = nn.AvgPool1d(kernel_size=2, stride=2)
print(avgpool(input_data))