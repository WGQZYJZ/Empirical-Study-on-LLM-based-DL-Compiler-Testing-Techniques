'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inner\ntorch.Tensor.inner(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(3, 4)
other = torch.rand(4)
output_tensor = input_tensor.inner(other)
print(output_tensor)