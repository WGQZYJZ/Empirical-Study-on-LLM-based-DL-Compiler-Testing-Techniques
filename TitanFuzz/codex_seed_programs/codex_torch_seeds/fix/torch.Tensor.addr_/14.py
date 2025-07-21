'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr_\ntorch.Tensor.addr_(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.randn(3, 3)
vec1 = torch.randn(3)
vec2 = torch.randn(3)
print('Task 3: Call the API torch.Tensor.addr_')
output_tensor = torch.Tensor.addr_(input_tensor, vec1, vec2, beta=1, alpha=1)
print(output_tensor)