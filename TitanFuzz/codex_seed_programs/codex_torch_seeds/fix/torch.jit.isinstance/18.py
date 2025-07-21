'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.isinstance\ntorch.jit.isinstance(obj, target_type)\n'
import torch
obj = torch.randn(3, 4)
target_type = torch.Tensor
result = torch.jit.isinstance(obj, target_type)
print(result)