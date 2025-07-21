'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.triu_\ntorch.Tensor.triu_(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.randn(2, 3, dtype=torch.float32)
print('Input tensor: {}'.format(input_tensor))
result = torch.Tensor.triu_(input_tensor, diagonal=0)
print('Result: {}'.format(result))