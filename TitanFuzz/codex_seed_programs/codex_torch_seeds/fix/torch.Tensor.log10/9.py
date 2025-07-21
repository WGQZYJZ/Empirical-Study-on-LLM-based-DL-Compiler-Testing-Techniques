'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log10\ntorch.Tensor.log10(_input_tensor)\n'
import torch
input_tensor = torch.randn(5, 5)
print('Input Tensor:')
print(input_tensor)
output_tensor = input_tensor.log10()
print('Output Tensor:')
print(output_tensor)