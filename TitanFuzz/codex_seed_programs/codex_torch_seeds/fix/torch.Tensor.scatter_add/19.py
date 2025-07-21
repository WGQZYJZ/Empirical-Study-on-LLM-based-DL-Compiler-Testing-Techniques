'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add\ntorch.Tensor.scatter_add(_input_tensor, dim, index, src)\n'
import torch
import torch
input_tensor = torch.randint(0, 10, (3, 3))
print('input_tensor:', input_tensor)
index = torch.tensor([0, 2, 1])
src = torch.tensor([1, 2, 3])
result = torch.Tensor.scatter_add(input_tensor, dim=0, index=index, src=src)
print('result:', result)