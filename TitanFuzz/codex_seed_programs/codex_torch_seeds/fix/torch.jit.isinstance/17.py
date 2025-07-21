'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.isinstance\ntorch.jit.isinstance(obj, target_type)\n'
import torch
x = torch.randn(5)
y = torch.randn(5, 3)
z = torch.randn(5, 3, 2)
print(torch.jit.isinstance(x, torch.Tensor))
print(torch.jit.isinstance(y, torch.Tensor))
print(torch.jit.isinstance(z, torch.Tensor))