'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.is_tensor_like\ntorch.overrides.is_tensor_like(inp)\n'
import torch
inp = [1, 2, 3]
inp_tensor = torch.tensor(inp)
print(torch.overrides.is_tensor_like(inp))
print(torch.overrides.is_tensor_like(inp_tensor))