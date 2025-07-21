'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.storage\ntorch.Tensor.storage(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input Tensor:', _input_tensor)
_storage = _input_tensor.storage()
print('Storage:', _storage)