'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.is_tensor_like\ntorch.overrides.is_tensor_like(inp)\n'
import torch
input_data = torch.rand(10, 10)
print(torch.overrides.is_tensor_like(input_data))
print(torch.overrides.is_tensor_like(1))
print(torch.overrides.is_tensor_like(1.0))
print(torch.overrides.is_tensor_like((1.0 + 1j)))
print(torch.overrides.is_tensor_like('hello'))
print(torch.overrides.is_tensor_like(True))
print(torch.overrides.is_tensor_like(None))
print(torch.overrides.is_tensor_like([]))
print(torch.overrides.is_tensor_like({}))
print(torch.overrides.is_tensor_like(()))
print(torch.overrides.is_tensor_like(set()))