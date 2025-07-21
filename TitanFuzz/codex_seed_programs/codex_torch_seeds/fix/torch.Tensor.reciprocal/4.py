'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal\ntorch.Tensor.reciprocal(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
output_tensor = torch.Tensor.reciprocal(input_tensor)
print(output_tensor)
'\nTask 4: Call the API torch.reciprocal\ntorch.reciprocal(_input_tensor)\n'
output_tensor = torch.reciprocal(input_tensor)
print(output_tensor)