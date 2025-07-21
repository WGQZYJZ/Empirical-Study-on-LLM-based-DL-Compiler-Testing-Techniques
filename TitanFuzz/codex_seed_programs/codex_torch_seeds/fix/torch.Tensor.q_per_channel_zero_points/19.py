'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_zero_points\ntorch.Tensor.q_per_channel_zero_points(_input_tensor)\n'
import torch
_input_tensor = torch.randint(low=0, high=255, size=(2, 3, 4, 5), dtype=torch.uint8)
output_tensor = _input_tensor.q_per_channel_zero_points()
print('input_tensor: ', _input_tensor)
print('output_tensor: ', output_tensor)