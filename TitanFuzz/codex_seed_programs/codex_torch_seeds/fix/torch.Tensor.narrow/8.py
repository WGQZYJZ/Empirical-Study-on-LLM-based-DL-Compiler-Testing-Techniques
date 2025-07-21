'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow\ntorch.Tensor.narrow(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('input_tensor: {}'.format(input_tensor))
print('torch.Tensor.narrow(input_tensor, 1, 0, 2): {}'.format(torch.Tensor.narrow(input_tensor, 1, 0, 2)))
print('torch.Tensor.narrow(input_tensor, 2, 1, 3): {}'.format(torch.Tensor.narrow(input_tensor, 2, 1, 3)))