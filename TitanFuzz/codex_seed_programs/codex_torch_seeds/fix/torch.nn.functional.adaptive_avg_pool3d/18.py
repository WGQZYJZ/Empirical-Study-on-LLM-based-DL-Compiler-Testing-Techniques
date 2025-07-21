'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool3d\ntorch.nn.functional.adaptive_avg_pool3d(input, output_size)\n'
import torch
import torch.nn.functional as F
x = torch.randn(2, 3, 4, 4, 4)
out = F.adaptive_avg_pool3d(x, (1, 1, 1))
print(out)
out = F.adaptive_max_pool3d(x, (1, 1, 1))
print(out)