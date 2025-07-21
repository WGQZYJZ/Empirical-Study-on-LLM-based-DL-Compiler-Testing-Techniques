'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
input = torch.randint(0, 10, (3, 3))
print(input)
result = torch.isfinite(input)
print(result)