'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inverse\ntorch.Tensor.inverse(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 2)
print('Input tensor:', input_tensor)
inverse_tensor = torch.Tensor.inverse(input_tensor)
print('Inverse tensor:', inverse_tensor)