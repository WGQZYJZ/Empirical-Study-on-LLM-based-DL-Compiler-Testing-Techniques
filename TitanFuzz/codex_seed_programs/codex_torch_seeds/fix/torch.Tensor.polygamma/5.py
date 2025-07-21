'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.polygamma\ntorch.Tensor.polygamma(_input_tensor, n)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = input_tensor.polygamma(1)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)