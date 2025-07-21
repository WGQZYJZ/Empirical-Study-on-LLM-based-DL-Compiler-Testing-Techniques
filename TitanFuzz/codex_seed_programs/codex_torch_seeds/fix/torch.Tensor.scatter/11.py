'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor:', input_tensor)
index = torch.tensor([[0, 1, 2], [1, 2, 0]])
src = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = torch.Tensor.scatter(input_tensor, dim=0, index=index, src=src)
print('Output tensor:', output)