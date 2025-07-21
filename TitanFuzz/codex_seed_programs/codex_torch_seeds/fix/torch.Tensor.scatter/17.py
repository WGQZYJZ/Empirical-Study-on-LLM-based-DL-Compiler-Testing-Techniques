'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
index = torch.tensor([[0, 1, 0], [1, 0, 1]])
src = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.scatter(input_tensor, 0, index, src)
print(output_tensor)