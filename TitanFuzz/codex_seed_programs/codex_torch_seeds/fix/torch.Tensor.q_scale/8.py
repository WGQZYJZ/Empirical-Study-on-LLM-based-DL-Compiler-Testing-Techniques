'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_scale\ntorch.Tensor.q_scale(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.randn(1, 3, 224, 224)
output_tensor = torch.Tensor.q_scale(input_tensor)
print('Input tensor: ', input_tensor)
print('Output tensor: ', output_tensor)