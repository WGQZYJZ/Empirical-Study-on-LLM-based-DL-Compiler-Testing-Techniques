'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapaxes\ntorch.Tensor.swapaxes(_input_tensor, axis0, axis1)\n'
import torch
input_tensor = torch.randn(3, 4, 5)
print('Input tensor: \n{}'.format(input_tensor))
output_tensor = input_tensor.swapaxes(0, 2)
print('Output tensor: \n{}'.format(output_tensor))