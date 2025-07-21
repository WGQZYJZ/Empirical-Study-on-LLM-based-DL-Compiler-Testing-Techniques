'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log2\ntorch.Tensor.log2(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.log2()
print('Output tensor: ', output_tensor)