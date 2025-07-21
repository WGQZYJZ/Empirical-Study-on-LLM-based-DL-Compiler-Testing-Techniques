'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_zero_points\ntorch.Tensor.q_per_channel_zero_points(_input_tensor)\n'
import torch
import torch.quantization
from torch.quantization import QuantStub, DeQuantStub
import torch
input_tensor = torch.tensor([[1.2, 3.4], [5.6, 7.8]])
print('input_tensor: ', input_tensor)
print('torch.Tensor.q_per_channel_zero_points(input_tensor): ', torch.Tensor.q_per_channel_zero_points(input_tensor))