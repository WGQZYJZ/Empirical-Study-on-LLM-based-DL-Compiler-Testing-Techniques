'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp_\ntorch.Tensor.lerp_(_input_tensor, end, weight)\n'
import torch
input_tensor = torch.randn(3, 3)
end = torch.randn(3, 3)
weight = torch.rand(1)
output_tensor = torch.Tensor.lerp_(input_tensor, end, weight)
print('input_tensor: ', input_tensor)
print('end: ', end)
print('weight: ', weight)
print('output_tensor: ', output_tensor)