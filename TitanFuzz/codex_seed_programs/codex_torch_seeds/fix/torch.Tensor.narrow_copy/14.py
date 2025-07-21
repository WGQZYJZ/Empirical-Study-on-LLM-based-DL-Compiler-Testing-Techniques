'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow_copy\ntorch.Tensor.narrow_copy(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.rand(4, 4)
print(input_tensor)
output_tensor = torch.Tensor.narrow_copy(input_tensor, 1, 1, 2)
print(output_tensor)