'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_zero_points\ntorch.Tensor.q_per_channel_zero_points(_input_tensor)\n'
import torch
from torch.autograd import Variable
import torch
input_data = torch.randn(2, 3, 4)
output_data = torch.Tensor.q_per_channel_zero_points(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)