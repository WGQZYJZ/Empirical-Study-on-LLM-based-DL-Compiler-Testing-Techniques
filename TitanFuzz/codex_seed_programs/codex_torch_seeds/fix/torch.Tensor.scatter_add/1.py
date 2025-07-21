'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add\ntorch.Tensor.scatter_add(_input_tensor, dim, index, src)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dim = 1
index = torch.tensor([0, 1, 2])
src = torch.tensor([1, 2, 3])
result = _input_tensor.scatter_add(dim, index, src)
print(result)