'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tril\ntorch.Tensor.tril(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.tril(input_tensor, diagonal=0)
print(output_tensor)