'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tril_\ntorch.Tensor.tril_(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
torch.Tensor.tril_(input_tensor, diagonal=0)
print('Input tensor:')
print(input_tensor)
print('\n')