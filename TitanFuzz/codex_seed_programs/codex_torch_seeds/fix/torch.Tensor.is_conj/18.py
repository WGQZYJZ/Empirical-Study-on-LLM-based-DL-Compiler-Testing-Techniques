'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_conj\ntorch.Tensor.is_conj(_input_tensor)\n'
import torch
import torch
input_tensor = torch.rand(2, 3)
output_tensor = torch.Tensor.is_conj(input_tensor)
print('input_tensor = ', input_tensor)
print('output_tensor = ', output_tensor)