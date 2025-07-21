'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tile\ntorch.Tensor.tile(_input_tensor, dims)\n'
import torch
input_tensor = torch.randn(3, 5)
print(input_tensor)
output_tensor = torch.Tensor.tile(input_tensor, dims=(2, 3))
print(output_tensor)
output_tensor = torch.Tensor.tile(input_tensor, dims=(1, 3))
print(output_tensor)