'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.acos\ntorch.Tensor.acos(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input Tensor:')
print(input_tensor)
output_tensor = input_tensor.acos()
print('Output Tensor:')
print(output_tensor)