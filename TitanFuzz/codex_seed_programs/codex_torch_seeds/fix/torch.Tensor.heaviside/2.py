'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
input_tensor = torch.randn(3, 3)
print('input_tensor:', input_tensor)
print('torch.Tensor.heaviside(input_tensor, values):', torch.Tensor.heaviside(input_tensor, values=0))