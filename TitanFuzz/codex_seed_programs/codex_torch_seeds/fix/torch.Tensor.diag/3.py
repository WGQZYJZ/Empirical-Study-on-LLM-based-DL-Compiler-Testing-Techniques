'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diag\ntorch.Tensor.diag(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = input_tensor.diag()
print(output_tensor)
output_tensor = input_tensor.diag(diagonal=1)
print(output_tensor)
output_tensor = input_tensor.diag(diagonal=(- 1))
print(output_tensor)