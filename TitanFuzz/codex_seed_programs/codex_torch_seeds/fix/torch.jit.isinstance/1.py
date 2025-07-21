'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.isinstance\ntorch.jit.isinstance(obj, target_type)\n'
import torch
x = torch.randn(3, 4)
print(torch.jit.isinstance(x, torch.Tensor))