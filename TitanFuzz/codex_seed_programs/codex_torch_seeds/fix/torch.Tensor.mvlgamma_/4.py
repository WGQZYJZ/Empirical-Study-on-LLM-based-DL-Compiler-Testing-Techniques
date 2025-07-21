'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mvlgamma_\ntorch.Tensor.mvlgamma_(_input_tensor, p)\n'
import torch
input_tensor = torch.rand(100, 100)
output_tensor = torch.Tensor.mvlgamma_(input_tensor, p=2)
print('Input tensor: ', input_tensor)
print('Output tensor: ', output_tensor)