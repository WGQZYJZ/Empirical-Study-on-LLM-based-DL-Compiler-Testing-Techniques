'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isreal\ntorch.Tensor.isreal(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
real_tensor = torch.Tensor.isreal(input_tensor)
print('The input tensor is real: {}'.format(real_tensor))
input_tensor = (torch.randn(4, 4) + (1j * torch.randn(4, 4)))
real_tensor = torch.Tensor.isreal(input_tensor)
print('The input tensor is real: {}'.format(real_tensor))