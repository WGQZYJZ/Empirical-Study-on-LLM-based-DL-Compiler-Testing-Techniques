'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add_\ntorch.Tensor.index_add_(_input_tensor, dim, index, tensor, *, alpha=1)\n'
import torch
import torch
input_tensor = torch.ones(3, 4)
index = torch.tensor([0, 2])
tensor = torch.tensor([[2, 2, 2, 2], [3, 3, 3, 3]])
print('Input tensor:')
print(input_tensor)
print('Input index:')
print(index)
print('Input tensor:')
print(tensor)
torch.Tensor.index_add_(input_tensor, dim=0, index=index, tensor=tensor)
print('Output tensor:')
print(input_tensor)