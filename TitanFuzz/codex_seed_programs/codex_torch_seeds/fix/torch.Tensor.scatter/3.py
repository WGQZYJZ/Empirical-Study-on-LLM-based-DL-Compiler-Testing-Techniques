'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
x = torch.randn(3, 4)
print(x)
index = torch.tensor([[0, 2], [2, 0]])
src = torch.tensor([[1, 2], [3, 4]])
print(torch.Tensor.scatter(x, 0, index, src))