'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp_\ntorch.Tensor.lerp_(_input_tensor, end, weight)\n'
import torch
input_tensor = torch.rand(2, 3)
end = torch.rand(2, 3)
weight = torch.rand(2, 3)
torch.Tensor.lerp_(input_tensor, end, weight)
print('Input tensor: ', input_tensor)
print('End tensor: ', end)
print('Weight tensor: ', weight)
print('Output tensor: ', input_tensor)