'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.isinstance\ntorch.jit.isinstance(obj, target_type)\n'
import torch
data = torch.randn(2, 3)
output = torch.jit.isinstance(data, torch.Tensor)
print(output)