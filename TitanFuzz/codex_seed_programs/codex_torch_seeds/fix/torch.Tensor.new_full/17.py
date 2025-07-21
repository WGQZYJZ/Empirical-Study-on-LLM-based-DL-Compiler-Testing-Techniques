'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_full\ntorch.Tensor.new_full(_input_tensor, size, fill_value, dtype=None, device=None, requires_grad=False)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('\nTask 2: Generate input data')
input_tensor = torch.randn(3, 3)
print('input_tensor: ', input_tensor)
print('\nTask 3: Call the API torch.Tensor.new_full')
output_tensor = torch.Tensor.new_full(input_tensor, size=[2, 3], fill_value=1)
print('output_tensor: ', output_tensor)