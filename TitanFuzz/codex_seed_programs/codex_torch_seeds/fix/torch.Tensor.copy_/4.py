'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.copy_\ntorch.Tensor.copy_(_input_tensor, src, non_blocking=False)\n'
import torch
import torch
_input_tensor = torch.randint(10, (4, 5))
_input_tensor = torch.randint(10, (4, 5))
print('Input tensor: ', _input_tensor)
_input_tensor.copy_(torch.randint(10, (4, 5)))
print('Output tensor: ', _input_tensor)