'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp\ntorch.Tensor.lerp(_input_tensor, end, weight)\n'
import torch
input_tensor = torch.rand(2, 3)
end = torch.rand(2, 3)
weight = 0.5
output_tensor = input_tensor.lerp(end, weight)
print('input_tensor: ', input_tensor)
print('end: ', end)
print('weight: ', weight)
print('output_tensor: ', output_tensor)