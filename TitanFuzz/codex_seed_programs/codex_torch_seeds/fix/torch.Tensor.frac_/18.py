'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac_\ntorch.Tensor.frac_(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input Tensor:')
print(input_tensor)
torch.Tensor.frac_(input_tensor)
print('Output Tensor:')
print(input_tensor)