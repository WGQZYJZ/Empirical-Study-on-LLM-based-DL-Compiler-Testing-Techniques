'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal\ntorch.Tensor.reciprocal(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, dtype=torch.float32)
reciprocal_tensor = torch.Tensor.reciprocal(input_tensor)
print('Input Tensor: ', input_tensor)
print('Reciprocal Tensor: ', reciprocal_tensor)