'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.isinstance\ntorch.jit.isinstance(obj, target_type)\n'
import torch
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])
z = torch.tensor([7, 8, 9])
print(torch.jit.isinstance(x, torch.Tensor))
print(torch.jit.isinstance(y, torch.Tensor))
print(torch.jit.isinstance(z, torch.Tensor))