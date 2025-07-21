'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.heaviside(input_tensor, values=(0.5, 1.5))
print('input_tensor:')
print(input_tensor)
print('output_tensor:')
print(output_tensor)