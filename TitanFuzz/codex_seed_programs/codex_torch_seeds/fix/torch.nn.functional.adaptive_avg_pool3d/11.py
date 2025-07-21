'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool3d\ntorch.nn.functional.adaptive_avg_pool3d(input, output_size)\n'
import torch
import torch.nn.functional as F
dtype = torch.float
device = torch.device('cpu')
input = torch.randn(1, 3, 4, 4, 4, dtype=dtype, device=device, requires_grad=True)
output_size = (3, 3, 3)
output = F.adaptive_avg_pool3d(input, output_size)
print(output)