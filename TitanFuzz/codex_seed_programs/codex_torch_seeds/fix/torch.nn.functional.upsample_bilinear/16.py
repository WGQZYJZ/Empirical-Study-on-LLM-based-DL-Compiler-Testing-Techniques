'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_bilinear\ntorch.nn.functional.upsample_bilinear(input, size=None, scale_factor=None)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
input = torch.rand(1, 1, 4, 4)
output = F.upsample_bilinear(input, size=(8, 8))
print(output)