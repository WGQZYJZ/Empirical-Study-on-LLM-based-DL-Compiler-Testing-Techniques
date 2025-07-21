'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative\ntorch.Tensor.negative(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.negative(input_tensor)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)