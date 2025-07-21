'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac_\ntorch.Tensor.frac_(_input_tensor)\n'
import torch
input_data = torch.rand(2, 3)
print('Input data:')
print(input_data)
print('\nOutput data:')
print(torch.Tensor.frac_(input_data))