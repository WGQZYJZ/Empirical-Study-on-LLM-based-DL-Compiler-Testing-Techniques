'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_zero_points\ntorch.Tensor.q_per_channel_zero_points(_input_tensor)\n'
import torch
input_tensor = torch.rand(1, 3, 4, 4, dtype=torch.float32)
output_tensor = torch.Tensor.q_per_channel_zero_points(input_tensor)
print('Input tensor: \n', input_tensor)
print('Output tensor: \n', output_tensor)