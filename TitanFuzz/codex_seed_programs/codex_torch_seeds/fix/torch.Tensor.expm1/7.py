'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expm1\ntorch.Tensor.expm1(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
output_tensor = input_tensor.expm1()
print(output_tensor)