'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool3d\ntorch.nn.functional.adaptive_avg_pool3d(input, output_size)\n'
import torch
input = torch.rand(1, 3, 4, 4, 4)
output_size = (2, 2, 2)
import torch
input = torch.rand(1, 3, 4, 4, 4)
output = torch.nn.functional.adaptive_avg_pool3d(input, output_size)
print(output)