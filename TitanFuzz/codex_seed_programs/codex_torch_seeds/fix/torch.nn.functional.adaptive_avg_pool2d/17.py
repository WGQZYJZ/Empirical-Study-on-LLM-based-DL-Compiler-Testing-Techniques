'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool2d\ntorch.nn.functional.adaptive_avg_pool2d(input, output_size)\n'
import torch
input_data = torch.randn(1, 1, 64, 64)
output_size = (4, 4)
output = torch.nn.functional.adaptive_avg_pool2d(input_data, output_size)
print(output)
print(output.shape)