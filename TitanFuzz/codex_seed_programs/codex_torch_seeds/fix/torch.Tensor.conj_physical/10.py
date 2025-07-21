'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj_physical\ntorch.Tensor.conj_physical(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
print('input_tensor:', input_tensor)
output_tensor = torch.Tensor.conj_physical(input_tensor)
print('output_tensor:', output_tensor)