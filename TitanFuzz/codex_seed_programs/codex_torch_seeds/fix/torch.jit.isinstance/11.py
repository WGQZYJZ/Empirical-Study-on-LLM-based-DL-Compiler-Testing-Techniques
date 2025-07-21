'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.isinstance\ntorch.jit.isinstance(obj, target_type)\n'
import torch
input = torch.rand(2, 3)
print(torch.jit.isinstance(input, torch.Tensor))