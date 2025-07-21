'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
import torch
input_tensor = torch.randn(10, 10)
output_tensor = torch.Tensor.isinf(input_tensor)
print(input_tensor)
print(output_tensor)