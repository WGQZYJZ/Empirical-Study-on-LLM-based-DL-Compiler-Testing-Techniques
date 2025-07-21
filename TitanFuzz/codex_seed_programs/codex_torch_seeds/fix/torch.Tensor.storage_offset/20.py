'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.storage_offset\ntorch.Tensor.storage_offset(_input_tensor)\n'
import torch
_input_tensor = torch.randn(10, 10)
print(torch.Tensor.storage_offset(_input_tensor))