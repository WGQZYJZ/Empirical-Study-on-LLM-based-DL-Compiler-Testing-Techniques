'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_axis\ntorch.Tensor.q_per_channel_axis(_input_tensor)\n'
import torch
import numpy as np
import torch
input_tensor = torch.randn(1, 3, 32, 32)
torch.Tensor.q_per_channel_axis(input_tensor)
print(input_tensor.q_per_channel_axis())
input_tensor = torch.randn(1, 3, 32, 32)
torch.Tensor.q_per_channel_axis(input_tensor, axis=2)
print(input_tensor.q_per_channel_axis(axis=2))
input_tensor = torch.randn(1, 3, 32, 32)