'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose_\ntorch.Tensor.transpose_(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.transpose_(input_tensor, 0, 1)
print('The result is: ', input_tensor)