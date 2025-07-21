'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.asin_\ntorch.Tensor.asin_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input Tensor: ', input_tensor)
output_tensor = torch.Tensor.asin_(input_tensor)
print('Output Tensor: ', output_tensor)