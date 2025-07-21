'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.is_tensor_like\ntorch.overrides.is_tensor_like(inp)\n'
import torch
inp = torch.randn(1, 1, 2, 2)
torch.overrides.is_tensor_like(inp)
torch.overrides.is_tensor_like(inp.tolist())