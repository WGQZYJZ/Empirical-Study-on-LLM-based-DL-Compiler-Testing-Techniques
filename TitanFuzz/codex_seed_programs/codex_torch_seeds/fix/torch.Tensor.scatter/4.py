'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
data = torch.randn(3, 4)
print(data)
index = torch.tensor([[0, 1], [1, 2]])
src = torch.tensor([[1, 2], [3, 4]])
print(torch.Tensor.scatter(data, 0, index, src))