'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inverse\ntorch.Tensor.inverse(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: \n', input_tensor)
inverse_tensor = input_tensor.inverse()
print('Inverse tensor: \n', inverse_tensor)