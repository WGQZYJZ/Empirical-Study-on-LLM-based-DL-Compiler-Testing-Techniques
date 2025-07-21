'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach_\ntorch.Tensor.detach_(_input_tensor, )\n'
import torch
input_tensor = torch.randn(3, 4)
detached_tensor = torch.Tensor.detach_(input_tensor)
print(input_tensor)
print(detached_tensor)