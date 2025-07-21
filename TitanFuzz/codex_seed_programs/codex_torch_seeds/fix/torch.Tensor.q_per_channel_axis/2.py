'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_axis\ntorch.Tensor.q_per_channel_axis(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 4, 5, 6)
_output_tensor = torch.Tensor.q_per_channel_axis(_input_tensor)
print(_output_tensor)