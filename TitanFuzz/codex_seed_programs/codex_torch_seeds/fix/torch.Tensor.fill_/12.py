'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_\ntorch.Tensor.fill_(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input data:')
print(input_tensor)
torch.Tensor.fill_(input_tensor, 2)
print('Output data:')
print(input_tensor)