'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_select\ntorch.Tensor.index_select(_input_tensor, dim, index)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.Tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
index = torch.LongTensor([0, 2])
print('Task 3: Call the API torch.Tensor.index_select')
output_tensor = input_tensor.index_select(dim=0, index=index)
print('input_tensor:')
print(input_tensor)
print('index:')
print(index)
print('output_tensor:')
print(output_tensor)