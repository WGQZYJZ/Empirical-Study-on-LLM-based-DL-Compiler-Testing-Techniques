'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hardshrink\ntorch.Tensor.hardshrink(_input_tensor, lambd=0.5)\n'
import torch
input_tensor = torch.randn(2, 3, dtype=torch.float32)
print('Input data:')
print(input_tensor)
output_tensor = torch.Tensor.hardshrink(input_tensor, lambd=0.5)
print('Output data:')
print(output_tensor)