'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_axis\ntorch.Tensor.q_per_channel_axis(_input_tensor)\n'
import torch
import torch.quantization
input_tensor = torch.randn(3, 4, 5).float()
torch.Tensor.q_per_channel_axis(input_tensor)
print('input_tensor: ', input_tensor)
print('input_tensor.q_per_channel_axis: ', input_tensor.q_per_channel_axis)