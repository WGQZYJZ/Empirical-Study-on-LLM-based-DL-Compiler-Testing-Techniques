'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input:')
print(input_tensor)
print('Heaviside:')
print(torch.Tensor.heaviside(input_tensor, 0.5))