'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ldexp_\ntorch.Tensor.ldexp_(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(3, 3)
print('The input tensor is: ', input_tensor)
output_tensor = torch.Tensor.ldexp_(input_tensor, 2)
print('The output tensor is: ', output_tensor)