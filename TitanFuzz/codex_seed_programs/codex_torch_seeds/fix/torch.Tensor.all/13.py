'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.all\ntorch.Tensor.all(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: {}'.format(input_tensor))
print('Result of torch.Tensor.all(input_tensor): {}'.format(torch.Tensor.all(input_tensor)))
print('Result of torch.Tensor.all(input_tensor, dim=0): {}'.format(torch.Tensor.all(input_tensor, dim=0)))
print('Result of torch.Tensor.all(input_tensor, dim=1): {}'.format(torch.Tensor.all(input_tensor, dim=1)))
print('Result of torch.Tensor.all(input_tensor, dim=-1): {}'.format(torch.Tensor.all(input_tensor, dim=(- 1))))