'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arcsin_\ntorch.Tensor.arcsin_(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input data:')
print(input_tensor)
torch.Tensor.arcsin_(input_tensor)
print('Output data:')
print(input_tensor)