'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.abs_\ntorch.Tensor.abs_(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3)
print('Input tensor: ', input_tensor)
abs_tensor = input_tensor.abs_()
print('Absolute tensor: ', abs_tensor)