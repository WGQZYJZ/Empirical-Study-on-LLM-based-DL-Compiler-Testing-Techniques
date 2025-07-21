'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.is_tensor_like\ntorch.overrides.is_tensor_like(inp)\n'
import torch
inp = torch.rand(5, 3)
torch.overrides.is_tensor_like(inp)
torch.overrides.is_tensor_like(1)
torch.overrides.is_tensor_like([1, 2, 3])
torch.overrides.is_tensor_like(torch.tensor(1))
torch.overrides.is_tensor_like(torch.tensor([1, 2, 3]))