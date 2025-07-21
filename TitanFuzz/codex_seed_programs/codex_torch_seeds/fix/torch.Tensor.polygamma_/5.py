'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.polygamma_\ntorch.Tensor.polygamma_(_input_tensor, n)\n'
import torch
input_tensor = torch.randn(1, 2, 3)
output_tensor = torch.Tensor.polygamma_(input_tensor, 3)
print('Input Tensor: ', input_tensor)
print('Output Tensor: ', output_tensor)