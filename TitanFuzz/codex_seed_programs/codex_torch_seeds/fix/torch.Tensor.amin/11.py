'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amin\ntorch.Tensor.amin(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(4, 3)
print('Input Tensor:', input_tensor)
print('torch.Tensor.amin(input_tensor):', torch.Tensor.amin(input_tensor))
print('torch.Tensor.amin(input_tensor, dim=0):', torch.Tensor.amin(input_tensor, dim=0))
print('torch.Tensor.amin(input_tensor, dim=1):', torch.Tensor.amin(input_tensor, dim=1))