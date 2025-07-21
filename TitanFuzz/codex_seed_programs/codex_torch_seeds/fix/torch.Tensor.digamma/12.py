'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma\ntorch.Tensor.digamma(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3, 4)
print('input_data:\n', input_data)
print('torch.Tensor.digamma(input_data):\n', torch.Tensor.digamma(input_data))