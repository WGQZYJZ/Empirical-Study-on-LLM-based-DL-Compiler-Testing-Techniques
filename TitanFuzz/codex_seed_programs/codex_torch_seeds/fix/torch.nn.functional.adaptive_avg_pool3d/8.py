'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool3d\ntorch.nn.functional.adaptive_avg_pool3d(input, output_size)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 3, 10, 10, 10)
output_size = (5, 5, 5)
output = F.adaptive_avg_pool3d(input, output_size)
print(output)