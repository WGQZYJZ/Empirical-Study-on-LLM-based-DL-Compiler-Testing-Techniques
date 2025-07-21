'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.prod\ntorch.Tensor.prod(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor:')
print(input_tensor)
print('\ninput_tensor.prod(dim=0):')
print(input_tensor.prod(dim=0))
print('\ninput_tensor.prod(dim=1):')
print(input_tensor.prod(dim=1))
print('\ninput_tensor.prod(dim=1, keepdim=True):')
print(input_tensor.prod(dim=1, keepdim=True))
print('\ninput_tensor.prod(dim=-1):')
print(input_tensor.prod(dim=(- 1)))
print('\ninput_tensor.prod(dim=-1, keepdim=True):')
print(input_tensor.prod(dim=(- 1), keepdim=True))
print('\ninput_tensor.prod(dim=0, dtype=torch.float16):')
print