'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mvlgamma\ntorch.Tensor.mvlgamma(_input_tensor, p)\n'
import torch
input_tensor = torch.randn(2, 3)
output_tensor = input_tensor.mvlgamma(1)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)