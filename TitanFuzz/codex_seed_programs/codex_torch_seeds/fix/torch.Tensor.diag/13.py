'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diag\ntorch.Tensor.diag(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(3, 3))
diagonal_tensor = input_tensor.diag(diagonal=0)
print(diagonal_tensor)