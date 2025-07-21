'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_zero_points\ntorch.Tensor.q_per_channel_zero_points(_input_tensor)\n'
import torch
input_tensor = torch.arange(1, 17, dtype=torch.float32).reshape(1, 1, 4, 4)
output = torch.Tensor.q_per_channel_zero_points(input_tensor)
print(output)