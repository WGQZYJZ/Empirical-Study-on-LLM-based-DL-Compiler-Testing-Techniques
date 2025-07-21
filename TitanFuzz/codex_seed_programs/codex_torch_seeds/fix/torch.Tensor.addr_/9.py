'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr_\ntorch.Tensor.addr_(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.randn(2, 3)
vec1 = torch.randn(3)
vec2 = torch.randn(3)
output_tensor = torch.Tensor.addr_(input_tensor, vec1, vec2, beta=1.0, alpha=1.0)
print('input_tensor: ', input_tensor)
print('vec1: ', vec1)
print('vec2: ', vec2)
print('output_tensor: ', output_tensor)