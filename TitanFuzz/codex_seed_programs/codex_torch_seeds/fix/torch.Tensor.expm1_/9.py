'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expm1_\ntorch.Tensor.expm1_(_input_tensor)\n'
import torch
input_tensor = torch.randn(100, 100)
output_tensor = input_tensor.expm1_()
print(output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.exponential_\ntorch.Tensor.exponential_(lambd=1, _input_tensor)\n'
import torch
input_tensor = torch.randn(100, 100)
output_tensor = input_tensor.exponential_(lambd=1)
print(output_tensor)