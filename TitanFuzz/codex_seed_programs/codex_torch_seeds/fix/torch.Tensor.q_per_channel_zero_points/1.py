'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_zero_points\ntorch.Tensor.q_per_channel_zero_points(_input_tensor)\n'
import torch
input_data = torch.randn(3, 3)
print(input_data)
print(torch.Tensor.q_per_channel_zero_points(input_data))