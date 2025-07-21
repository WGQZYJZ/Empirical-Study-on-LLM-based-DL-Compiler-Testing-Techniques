'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.eq\ntorch.Tensor.eq(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(1, 3)
other = torch.randn(1, 3)
output_tensor = input_tensor.eq(other)
print(output_tensor)