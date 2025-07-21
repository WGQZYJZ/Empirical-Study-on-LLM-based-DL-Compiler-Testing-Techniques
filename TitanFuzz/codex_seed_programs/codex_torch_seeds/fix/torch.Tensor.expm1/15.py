'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expm1\ntorch.Tensor.expm1(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('The input tensor is: ', input_tensor)
output_tensor = torch.Tensor.expm1(input_tensor)
print('The output tensor is: ', output_tensor)