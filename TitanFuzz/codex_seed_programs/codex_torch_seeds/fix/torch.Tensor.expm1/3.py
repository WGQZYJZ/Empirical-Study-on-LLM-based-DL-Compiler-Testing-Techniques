'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expm1\ntorch.Tensor.expm1(_input_tensor)\n'
import torch
input_data = torch.rand(3, 3)
print(input_data)
output_data = torch.Tensor.expm1(input_data)
print(output_data)