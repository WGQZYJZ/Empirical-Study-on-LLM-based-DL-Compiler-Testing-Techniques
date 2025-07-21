'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tensor_split\ntorch.Tensor.tensor_split(_input_tensor, indices_or_sections, dim=0)\n'
import torch
input_tensor = torch.randn(5, 3, 4)
print('Input tensor: ')
print(input_tensor)
print('\nSplit the input tensor into 3 tensors along dim=1: ')
print(torch.Tensor.tensor_split(input_tensor, 3, dim=1))
print('\nSplit the input tensor into 2 tensors along dim=2: ')
print(torch.Tensor.tensor_split(input_tensor, 2, dim=2))
print('\nSplit the input tensor into 2 tensors along dim=0: ')
print(torch.Tensor.tensor_split(input_tensor, 2, dim=0))
print('\nSplit the input tensor into 3 tensors along dim=0: ')
print(torch.Tensor.tensor_split(input_tensor, 3, dim=0))