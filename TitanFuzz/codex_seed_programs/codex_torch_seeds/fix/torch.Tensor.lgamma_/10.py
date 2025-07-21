'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lgamma_\ntorch.Tensor.lgamma_(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print('Input tensor is: ', input_tensor)
output_tensor = input_tensor.lgamma_()
print('Output tensor is: ', output_tensor)