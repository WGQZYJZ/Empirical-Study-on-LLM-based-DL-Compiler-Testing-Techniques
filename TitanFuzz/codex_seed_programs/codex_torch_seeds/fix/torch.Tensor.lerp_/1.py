'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp_\ntorch.Tensor.lerp_(_input_tensor, end, weight)\n'
import torch
input_tensor = torch.rand(2, 3)
end = torch.rand(2, 3)
weight = torch.rand(2, 3)
output_tensor = torch.Tensor.lerp_(input_tensor, end, weight)
print('Input Tensor: ', input_tensor)
print('End Tensor: ', end)
print('Weight Tensor: ', weight)
print('Output Tensor: ', output_tensor)