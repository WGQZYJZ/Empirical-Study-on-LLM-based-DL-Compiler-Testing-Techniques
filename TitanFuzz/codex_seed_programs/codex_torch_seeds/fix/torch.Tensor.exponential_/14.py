'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.exponential_\ntorch.Tensor.exponential_(_input_tensor, lambd=1, *, generator=None)\n'
import torch
input_tensor = torch.rand(10)
print(input_tensor)
output_tensor = torch.Tensor.exponential_(input_tensor, lambd=1, generator=None)
print(output_tensor)