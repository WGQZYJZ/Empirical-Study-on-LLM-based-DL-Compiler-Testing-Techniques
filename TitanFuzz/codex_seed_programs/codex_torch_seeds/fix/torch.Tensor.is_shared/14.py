'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_shared\ntorch.Tensor.is_shared(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(1, 1)
is_shared = _input_tensor.is_shared()
print('is_shared: ', is_shared)