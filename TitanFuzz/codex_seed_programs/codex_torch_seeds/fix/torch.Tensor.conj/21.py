'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj\ntorch.Tensor.conj(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = input_tensor.conj()
print('input_tensor: \n', input_tensor)
print('output_tensor: \n', output_tensor)