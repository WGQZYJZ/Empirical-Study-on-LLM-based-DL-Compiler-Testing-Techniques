'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool3d\ntorch.nn.functional.adaptive_avg_pool3d(input, output_size)\n'
import torch
input = torch.randn(1, 64, 8, 8, 8)
output_size = (4, 4, 4)
output = torch.nn.functional.adaptive_avg_pool3d(input, output_size)
print(output.shape)