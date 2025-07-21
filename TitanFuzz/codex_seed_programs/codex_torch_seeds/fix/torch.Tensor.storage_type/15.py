'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.storage_type\ntorch.Tensor.storage_type(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
print(_input_tensor)
print(_input_tensor.storage_type())