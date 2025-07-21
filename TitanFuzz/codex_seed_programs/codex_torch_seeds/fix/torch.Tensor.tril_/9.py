'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tril_\ntorch.Tensor.tril_(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor: ')
print(input_tensor)
'\nTask 4: Call the API torch.Tensor.tril_\ntorch.Tensor.tril_(_input_tensor, diagonal=0)\n'
print('Output Tensor: ')
print(input_tensor.tril_())