'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.copy_\ntorch.Tensor.copy_(_input_tensor, src, non_blocking=False)\n'
import torch
input_tensor = torch.rand(100, 100)
input_data = torch.rand(100, 100)
torch.Tensor.copy_(input_tensor, input_data, non_blocking=False)
print(input_tensor)
print(input_data)