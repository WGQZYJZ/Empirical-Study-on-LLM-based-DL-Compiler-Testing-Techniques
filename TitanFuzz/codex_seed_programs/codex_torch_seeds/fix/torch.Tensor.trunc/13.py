'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('The input tensor is: ')
print(input_tensor)
print('The truncated tensor is: ')
print(input_tensor.trunc())