'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac\ntorch.Tensor.frac(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.frac(input_tensor)
print('Output tensor: ', output_tensor)
print('Fractional part of the input tensor: ', output_tensor)
print('Fractional part of the input tensor: ', output_tensor)