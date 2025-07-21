'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_storage\ntorch.is_storage(obj)\n'
import torch
inp = torch.randn(3, 3)
print(inp)
print(torch.is_storage(inp))