'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj\ntorch.Tensor.conj(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor:')
print(input_tensor)
output_tensor = torch.Tensor.conj(input_tensor)
print('Output tensor:')
print(output_tensor)