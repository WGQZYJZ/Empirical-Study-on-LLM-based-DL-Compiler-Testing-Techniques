'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clone\ntorch.Tensor.clone(_input_tensor, *, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.rand(3, 3)
print('Input tensor is: ', _input_tensor)
_clone_tensor = torch.Tensor.clone(_input_tensor)
print('Clone tensor is: ', _clone_tensor)