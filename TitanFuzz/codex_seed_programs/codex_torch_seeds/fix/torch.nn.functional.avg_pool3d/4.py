'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool3d\ntorch.nn.functional.avg_pool3d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
input = torch.rand(1, 1, 5, 5, 5)
output = F.avg_pool3d(input, kernel_size=3, stride=1, padding=1)
print(output)