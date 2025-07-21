'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take_along_dim\ntorch.Tensor.take_along_dim(_input_tensor, indices, dim)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
indices = torch.tensor([1, 0, 0, 1])
dim = 1
output_tensor = torch.Tensor.take_along_dim(input_tensor, indices, dim)
print(output_tensor)