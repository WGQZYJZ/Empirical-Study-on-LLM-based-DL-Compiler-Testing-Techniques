'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.msort\ntorch.Tensor.msort(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print('Input Tensor:\n', input_tensor)
print('\n')
print('Sorted Tensor:\n', torch.Tensor.msort(input_tensor))