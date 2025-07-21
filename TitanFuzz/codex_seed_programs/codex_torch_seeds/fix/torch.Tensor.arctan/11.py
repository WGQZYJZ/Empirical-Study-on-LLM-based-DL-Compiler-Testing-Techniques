'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctan\ntorch.Tensor.arctan(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 4, 5)
output_tensor = input_tensor.arctan()
print('input_tensor: \n', input_tensor)
print('output_tensor: \n', output_tensor)