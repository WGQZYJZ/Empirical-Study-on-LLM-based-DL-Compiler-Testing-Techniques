'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardswish\ntorch.nn.functional.hardswish(input, inplace=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 2, 3, 3)
output = F.hardswish(input)
print(output)