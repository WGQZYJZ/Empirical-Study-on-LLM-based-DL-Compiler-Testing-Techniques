'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool2d\ntorch.nn.functional.adaptive_avg_pool2d(input, output_size)\n'
import torch
import numpy as np
import torch
input_data = torch.rand(1, 1, 4, 4)
output_size = (1, 1)
torch.nn.functional.adaptive_avg_pool2d(input_data, output_size)
print(torch.nn.functional.adaptive_avg_pool2d(input_data, output_size))
print(torch.nn.functional.adaptive_avg_pool2d(input_data, output_size).size())