'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool2d\ntorch.nn.functional.adaptive_avg_pool2d(input, output_size)\n'
import torch
import torch.nn.functional as F
input_data = torch.rand(1, 1, 10, 10)
output_size = (5, 5)
output_data = F.adaptive_avg_pool2d(input_data, output_size)
print(output_data)