'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rot90\ntorch.Tensor.rot90(_input_tensor, k, dims)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('input_tensor = ', input_tensor)
output_tensor = torch.Tensor.rot90(input_tensor, k=1, dims=(0, 1))
print('output_tensor = ', output_tensor)