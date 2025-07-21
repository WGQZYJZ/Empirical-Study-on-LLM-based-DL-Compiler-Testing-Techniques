'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctan\ntorch.Tensor.arctan(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 5)
print('Input data:')
print(input_tensor)
output_tensor = torch.Tensor.arctan(input_tensor)
print('Output data:')
print(output_tensor)