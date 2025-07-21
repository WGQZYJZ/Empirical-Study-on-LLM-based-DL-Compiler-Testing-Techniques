'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take_along_dim\ntorch.Tensor.take_along_dim(_input_tensor, indices, dim)\n'
import torch
data = torch.arange(0, 100).reshape(10, 10)
indices = torch.tensor([[0, 1, 2, 3], [7, 8, 9, 4]])
result = torch.Tensor.take_along_dim(data, indices, dim=1)
print(result)