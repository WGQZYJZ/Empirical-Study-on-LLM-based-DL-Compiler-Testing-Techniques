'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clone\ntorch.Tensor.clone(_input_tensor, *, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(4, 4)
print('Input tensor: ', _input_tensor)
_cloned_tensor = _input_tensor.clone()
print('Cloned tensor: ', _cloned_tensor)