'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.aminmax\ntorch.Tensor.aminmax(_input_tensor, *, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.rand((3, 4))
print('Input Tensor: ')
print(input_tensor)
print('\nMin and Max values: ')
print(torch.Tensor.aminmax(input_tensor))
print('\nMin values: ')
print(torch.Tensor.aminmax(input_tensor, dim=0))
print('\nMax values: ')
print(torch.Tensor.aminmax(input_tensor, dim=1))