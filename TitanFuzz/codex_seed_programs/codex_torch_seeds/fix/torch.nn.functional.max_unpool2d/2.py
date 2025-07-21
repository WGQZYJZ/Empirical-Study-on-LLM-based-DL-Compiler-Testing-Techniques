'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_unpool2d\ntorch.nn.functional.max_unpool2d(input, indices, kernel_size, stride=None, padding=0, output_size=None)\n'
import torch
import torch.nn.functional as F
import torch
input = torch.ones([1, 1, 2, 2], dtype=torch.float)
indices = torch.ones([1, 1, 2, 2], dtype=torch.long)
output = F.max_unpool2d(input, indices, kernel_size=2, stride=1, padding=0)
print(output)