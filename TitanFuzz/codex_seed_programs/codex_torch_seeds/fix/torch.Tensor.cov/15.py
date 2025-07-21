'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cov\ntorch.Tensor.cov(_input_tensor, *, correction=1, fweights=None, aweights=None)\n'
import torch
input_data = torch.randn(3, 4)
print(input_data)
output_data = torch.Tensor.cov(input_data)
print(output_data)