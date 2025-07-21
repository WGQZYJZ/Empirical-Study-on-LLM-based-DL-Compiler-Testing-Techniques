'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool3d\ntorch.nn.functional.adaptive_avg_pool3d(input, output_size)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 1, 5, 5, 5)
output = F.adaptive_avg_pool3d(input, (3, 3, 3))
print(output)