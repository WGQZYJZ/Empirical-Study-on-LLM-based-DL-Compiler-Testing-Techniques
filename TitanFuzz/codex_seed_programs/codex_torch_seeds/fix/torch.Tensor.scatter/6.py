'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.rand(3, 5)
print(input_tensor)
indices = torch.tensor([0, 2])
values = torch.tensor([1, 2])
print(torch.Tensor.scatter(input_tensor, 0, indices, values))