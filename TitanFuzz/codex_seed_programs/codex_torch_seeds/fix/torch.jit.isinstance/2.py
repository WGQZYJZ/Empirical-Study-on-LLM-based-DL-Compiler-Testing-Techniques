'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.isinstance\ntorch.jit.isinstance(obj, target_type)\n'
import torch
import torch
input_data = torch.rand(1, 1, 3, 3)
print(torch.jit.isinstance(input_data, torch.Tensor))