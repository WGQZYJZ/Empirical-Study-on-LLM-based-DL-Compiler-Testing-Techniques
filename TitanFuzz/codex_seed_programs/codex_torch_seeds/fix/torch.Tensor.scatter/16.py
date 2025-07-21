'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
result = torch.Tensor.scatter(input_tensor, dim=1, index=torch.tensor([[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]), src=torch.tensor([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]]))
print(result)