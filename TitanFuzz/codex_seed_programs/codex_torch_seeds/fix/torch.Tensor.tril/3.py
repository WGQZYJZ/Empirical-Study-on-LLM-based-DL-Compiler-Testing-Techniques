'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tril\ntorch.Tensor.tril(_input_tensor, diagonal=0)\n'
import torch
import torch
input_tensor = torch.randn(3, 5)
tril_tensor = input_tensor.tril(diagonal=0)
print(tril_tensor)