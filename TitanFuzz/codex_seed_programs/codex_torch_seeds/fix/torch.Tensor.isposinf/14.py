'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isposinf\ntorch.Tensor.isposinf(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 4, 5)
output_tensor = input_tensor.isposinf()
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)