"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch
input = torch.randn(1, 1, 5, 5)
output = torch.nn.Upsample(size=(9, 9), mode='nearest')(input)
print(output)