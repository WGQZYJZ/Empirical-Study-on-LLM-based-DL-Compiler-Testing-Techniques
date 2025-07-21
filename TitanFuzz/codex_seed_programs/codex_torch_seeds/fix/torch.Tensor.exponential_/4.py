'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.exponential_\ntorch.Tensor.exponential_(_input_tensor, lambd=1, *, generator=None)\n'
import torch
input_data = torch.randn(3, 3)
print(input_data)
output_data = torch.Tensor.exponential_(input_data, lambd=1)
print(output_data)