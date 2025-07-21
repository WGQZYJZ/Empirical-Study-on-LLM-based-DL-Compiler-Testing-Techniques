'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_select\ntorch.Tensor.index_select(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([0, 2])
print(torch.Tensor.index_select(input_tensor, 0, index))