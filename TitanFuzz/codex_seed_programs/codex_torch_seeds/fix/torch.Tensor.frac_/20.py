'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac_\ntorch.Tensor.frac_(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
print('Input Tensor: ', input_tensor)
output_tensor = input_tensor.frac_()
print('Output Tensor: ', output_tensor)