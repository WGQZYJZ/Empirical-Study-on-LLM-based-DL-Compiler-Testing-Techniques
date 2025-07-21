'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.round_\ntorch.Tensor.round_(_input_tensor)\n'
import torch
input_tensor = torch.randn(10)
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.round_()
print('output_tensor: ', output_tensor)