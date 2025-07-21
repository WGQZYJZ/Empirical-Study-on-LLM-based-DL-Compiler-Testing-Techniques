'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_scale\ntorch.Tensor.q_scale(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = torch.Tensor.q_scale(input_tensor)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)