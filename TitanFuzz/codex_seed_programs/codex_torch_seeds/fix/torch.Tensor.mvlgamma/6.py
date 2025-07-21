'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mvlgamma\ntorch.Tensor.mvlgamma(_input_tensor, p)\n'
import torch
input_tensor = torch.rand(1, 3, 3)
p = 1
output_tensor = input_tensor.mvlgamma(p)
print('input tensor: ', input_tensor)
print('output tensor: ', output_tensor)