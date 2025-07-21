'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.instance_norm\ntorch.nn.functional.instance_norm(input, running_mean=None, running_var=None, weight=None, bias=None, use_input_stats=True, momentum=0.1, eps=1e-05)\n'
import torch
import torch.nn as nn
batch_size = 1
num_channels = 3
height = 4
width = 4
input = torch.randn(batch_size, num_channels, height, width)
output = nn.functional.instance_norm(input)
print(output)