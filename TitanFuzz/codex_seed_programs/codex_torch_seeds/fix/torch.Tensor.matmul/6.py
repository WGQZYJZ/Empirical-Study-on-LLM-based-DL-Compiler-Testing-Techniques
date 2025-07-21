'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matmul\ntorch.Tensor.matmul(_input_tensor, tensor2)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor = ', input_tensor)
output_tensor = torch.Tensor.matmul(input_tensor, torch.randn(3, 4))
print('output_tensor = ', output_tensor)