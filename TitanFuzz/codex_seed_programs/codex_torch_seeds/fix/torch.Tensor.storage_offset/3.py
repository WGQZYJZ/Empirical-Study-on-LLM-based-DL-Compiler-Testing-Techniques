'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.storage_offset\ntorch.Tensor.storage_offset(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
print(input_tensor.storage_offset())
input_tensor = torch.randn(3, 3, 2)
print(input_tensor)
print(input_tensor.storage_offset())