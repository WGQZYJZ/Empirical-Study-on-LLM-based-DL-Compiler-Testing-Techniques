'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add\ntorch.Tensor.scatter_add(_input_tensor, dim, index, src)\n'
import torch
import torch
input_tensor = torch.randint(0, 10, (4, 4))
print('Input tensor:\n{}'.format(input_tensor))
index = torch.tensor([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]])
src = torch.tensor([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
scatter_add_tensor = input_tensor.scatter_add(0, index, src)
print('Scatter add tensor:\n{}'.format(scatter_add_tensor))