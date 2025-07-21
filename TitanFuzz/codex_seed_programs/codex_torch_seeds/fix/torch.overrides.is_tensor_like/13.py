'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.is_tensor_like\ntorch.overrides.is_tensor_like(inp)\n'
import torch
inp = torch.rand(2, 3)
print(torch.overrides.is_tensor_like(inp))
print(torch.overrides.is_tensor_like(inp.numpy()))
print(torch.overrides.is_tensor_like(inp.tolist()))
print(torch.overrides.is_tensor_like(inp.data))
print(torch.overrides.is_tensor_like(inp.detach()))
print(torch.overrides.is_tensor_like(inp.detach().numpy()))
print(torch.overrides.is_tensor_like(inp.detach().tolist()))
print(torch.overrides.is_tensor_like(inp.detach().data))
print(torch.overrides.is_tensor_like(inp.cpu()))