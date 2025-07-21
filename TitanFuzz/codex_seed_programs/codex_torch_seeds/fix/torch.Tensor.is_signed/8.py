'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_signed\ntorch.Tensor.is_signed(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 5)
output_tensor = torch.Tensor.is_signed(input_tensor)
print(output_tensor)