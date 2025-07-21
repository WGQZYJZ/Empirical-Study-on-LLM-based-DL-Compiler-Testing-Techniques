'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
input = torch.randn(1, 2, 3)
print(input)
result = torch.isfinite(input)
print(result)