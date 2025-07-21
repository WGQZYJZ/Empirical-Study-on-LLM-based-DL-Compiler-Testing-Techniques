'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow_copy\ntorch.Tensor.narrow_copy(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.randn(4, 6)
print(input_tensor)
narrow_copy_tensor = torch.Tensor.narrow_copy(input_tensor, 1, 2, 3)
print(narrow_copy_tensor)