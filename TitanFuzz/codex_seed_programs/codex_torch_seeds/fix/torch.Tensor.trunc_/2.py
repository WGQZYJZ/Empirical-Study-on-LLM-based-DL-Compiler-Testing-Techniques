'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc_\ntorch.Tensor.trunc_(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: \n{}'.format(input_tensor))
output_tensor = input_tensor.trunc_()
print('Output tensor: \n{}'.format(output_tensor))