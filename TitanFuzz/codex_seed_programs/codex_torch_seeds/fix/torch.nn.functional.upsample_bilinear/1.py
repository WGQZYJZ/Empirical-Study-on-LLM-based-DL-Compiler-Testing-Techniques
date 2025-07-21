'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_bilinear\ntorch.nn.functional.upsample_bilinear(input, size=None, scale_factor=None)\n'
import torch
import torch
input = torch.randn(1, 1, 5, 5)
output = torch.nn.functional.upsample_bilinear(input, size=None, scale_factor=2)
print(output)
print(output.size())