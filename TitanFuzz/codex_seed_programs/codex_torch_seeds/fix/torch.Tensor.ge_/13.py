'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ge_\ntorch.Tensor.ge_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
print('input_tensor: ', input_tensor)
other = torch.tensor([[1, 1], [4, 4]])
print('other: ', other)
torch.Tensor.ge_(input_tensor, other)
print('output_tensor: ', input_tensor)