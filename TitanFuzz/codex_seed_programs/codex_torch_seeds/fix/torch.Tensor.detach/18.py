'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach\ntorch.Tensor.detach(_input_tensor, )\n'
import torch
input_tensor = torch.randn(10, 10)
detached_tensor = input_tensor.detach()
print('Input tensor:', input_tensor)
print('Detached tensor:', detached_tensor)