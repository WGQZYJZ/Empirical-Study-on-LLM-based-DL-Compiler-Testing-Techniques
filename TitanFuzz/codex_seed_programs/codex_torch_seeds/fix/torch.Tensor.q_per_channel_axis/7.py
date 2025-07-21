'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_axis\ntorch.Tensor.q_per_channel_axis(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]], dtype=torch.float32)
output_tensor = input_tensor.q_per_channel_axis(2.0, 0.5, 0, 0, torch.quint8)
print('input_tensor: \n', input_tensor)
print('output_tensor: \n', output_tensor)