'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_axis\ntorch.Tensor.q_per_channel_axis(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.randn(3, 3, 3)
output_tensor = torch.Tensor.q_per_channel_axis(input_tensor)
print(output_tensor)