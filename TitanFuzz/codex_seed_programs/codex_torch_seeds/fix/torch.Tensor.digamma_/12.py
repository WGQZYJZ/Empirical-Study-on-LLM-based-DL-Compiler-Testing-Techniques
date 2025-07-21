'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma_\ntorch.Tensor.digamma_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.digamma_(input_tensor)
print('input tensor: ', input_tensor)
print('output tensor: ', output_tensor)