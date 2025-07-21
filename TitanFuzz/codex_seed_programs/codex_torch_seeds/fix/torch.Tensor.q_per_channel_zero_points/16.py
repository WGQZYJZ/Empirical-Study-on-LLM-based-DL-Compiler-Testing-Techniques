'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_zero_points\ntorch.Tensor.q_per_channel_zero_points(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[3.0, (- 0.5), 2, 7], [4.0, 5.0, 4.0, 8.0]], requires_grad=True)
output_tensor = torch.Tensor.q_per_channel_zero_points(input_tensor)
print(output_tensor)