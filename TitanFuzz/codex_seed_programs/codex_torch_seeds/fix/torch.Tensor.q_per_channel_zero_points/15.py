'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_zero_points\ntorch.Tensor.q_per_channel_zero_points(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(4, 4, 4, 4)
output_tensor = torch.Tensor.q_per_channel_zero_points(input_tensor)
print('Output tensor: ', output_tensor)