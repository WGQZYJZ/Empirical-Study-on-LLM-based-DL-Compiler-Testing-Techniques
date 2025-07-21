'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input Tensor:\n', input_tensor)
output_tensor = torch.Tensor.heaviside(input_tensor, 0)
print('Output Tensor:\n', output_tensor)