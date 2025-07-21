'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand_as\ntorch.Tensor.expand_as(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
other_tensor = torch.randn(2, 3)
print(input_tensor)
print(other_tensor)
print(input_tensor.expand_as(other_tensor))