'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_conj\ntorch.Tensor.is_conj(_input_tensor)\n'
import torch
input_tensor = torch.rand(4, 4)
print('input_tensor:', input_tensor)
output_tensor = input_tensor.is_conj()
print('output_tensor:', output_tensor)