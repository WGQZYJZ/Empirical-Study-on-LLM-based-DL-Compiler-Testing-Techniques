'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow_copy\ntorch.Tensor.narrow_copy(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.randn(5, 5)
print(input_tensor)
output_tensor = torch.Tensor.narrow_copy(input_tensor, 0, 1, 3)
print(output_tensor)