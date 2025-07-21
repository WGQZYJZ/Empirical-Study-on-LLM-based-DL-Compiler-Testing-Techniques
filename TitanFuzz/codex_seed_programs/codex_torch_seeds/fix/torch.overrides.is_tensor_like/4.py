'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.is_tensor_like\ntorch.overrides.is_tensor_like(inp)\n'
import torch
inp = torch.rand(3, 3)
print(inp)
print(torch.overrides.is_tensor_like(inp))