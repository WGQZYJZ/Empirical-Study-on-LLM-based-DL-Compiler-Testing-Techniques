'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool3d\ntorch.nn.functional.adaptive_avg_pool3d(input, output_size)\n'
import torch
import torch.nn as nn
input_size = (1, 3, 32, 32, 32)
input_data = torch.rand(input_size)
output = nn.functional.adaptive_avg_pool3d(input_data, (2, 2, 2))
print(output)