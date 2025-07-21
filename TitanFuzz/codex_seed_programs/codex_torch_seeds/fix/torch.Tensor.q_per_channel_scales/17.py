'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_scales\ntorch.Tensor.q_per_channel_scales(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.randn(1, 2, 3, 4)
_output_tensor = torch.Tensor.q_per_channel_scales(_input_tensor)
print('Input: ', _input_tensor)
print('Output: ', _output_tensor)