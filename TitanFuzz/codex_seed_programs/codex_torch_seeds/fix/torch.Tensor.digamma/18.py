'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma\ntorch.Tensor.digamma(_input_tensor)\n'
import torch
input_tensor = torch.rand((2, 3))
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.digamma()
print('Output tensor: ', output_tensor)