'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctan_\ntorch.Tensor.arctan_(_input_tensor)\n'
import torch
input_tensor = torch.randn(10, 10)
output_tensor = input_tensor.arctan_()
print('input_tensor =', input_tensor)
print('output_tensor =', output_tensor)