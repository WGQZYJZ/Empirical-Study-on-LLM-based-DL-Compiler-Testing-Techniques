'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill_\ntorch.Tensor.index_fill_(_input_tensor, dim, index, value)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('input_tensor: \n', input_tensor)
torch.Tensor.index_fill_(input_tensor, 0, torch.tensor([1]), torch.tensor(0))
print('output_tensor: \n', input_tensor)