'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mvlgamma\ntorch.Tensor.mvlgamma(_input_tensor, p)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.mvlgamma(input_tensor, 3)
print('Output tensor: ', output_tensor)