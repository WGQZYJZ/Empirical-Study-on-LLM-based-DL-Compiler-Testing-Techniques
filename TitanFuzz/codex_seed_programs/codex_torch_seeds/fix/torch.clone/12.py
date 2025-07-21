'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clone\ntorch.clone(input, *, memory_format=torch.preserve_format)\n'
import torch
tensor = torch.randn(3, 3)
print('Tensor: \n', tensor)
print('\nClone: \n', torch.clone(tensor))
print('\nClone: \n', torch.clone(tensor, memory_format=torch.contiguous_format))