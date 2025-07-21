'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_zero_points\ntorch.Tensor.q_per_channel_zero_points(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.randn(2, 3, 4, 5)
zero_points = input_tensor.q_per_channel_zero_points()
print(zero_points)