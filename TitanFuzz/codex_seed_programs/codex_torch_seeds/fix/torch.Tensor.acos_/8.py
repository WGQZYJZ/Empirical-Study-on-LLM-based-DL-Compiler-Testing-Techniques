'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.acos_\ntorch.Tensor.acos_(_input_tensor)\n'
import torch
input_data = torch.randn(4, 4)
print('Input data:')
print(input_data)
torch.Tensor.acos_(input_data)
print('Output data:')
print(input_data)