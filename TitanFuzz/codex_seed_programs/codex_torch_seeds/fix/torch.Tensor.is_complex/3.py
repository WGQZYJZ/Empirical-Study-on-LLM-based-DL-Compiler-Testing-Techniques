'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_complex\ntorch.Tensor.is_complex(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 5)
output_tensor = input_tensor.is_complex()
print(output_tensor)