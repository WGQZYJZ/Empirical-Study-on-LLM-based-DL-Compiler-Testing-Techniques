'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub_\ntorch.Tensor.sub_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(5, 3)
print(input_tensor)
other_tensor = torch.randn(5, 3)
print(other_tensor)
print(input_tensor.sub(other_tensor))
print(input_tensor)
print(input_tensor.sub_(other_tensor))
print(input_tensor)