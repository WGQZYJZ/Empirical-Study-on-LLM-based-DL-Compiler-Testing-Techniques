'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Input tensor:')
print(input_tensor)
print('\n')
index = torch.tensor([[0, 2, 0], [0, 0, 1]])
src = torch.tensor([[1, 2, 3], [4, 5, 6]])
result = torch.Tensor.scatter(input_tensor, 0, index, src)
print('Result:')
print(result)