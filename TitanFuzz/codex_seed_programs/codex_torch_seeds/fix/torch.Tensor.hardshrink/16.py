'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hardshrink\ntorch.Tensor.hardshrink(_input_tensor, lambd=0.5)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
output_tensor = torch.Tensor.hardshrink(input_tensor, lambd=0.5)
print(output_tensor)