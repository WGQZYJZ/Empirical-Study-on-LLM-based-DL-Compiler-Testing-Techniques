'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.moveaxis\ntorch.Tensor.moveaxis(_input_tensor, source, destination)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print(input_tensor)
output_tensor = input_tensor.moveaxis(1, 2)
print(output_tensor)
output_tensor = input_tensor.moveaxis(2, 0)
print(output_tensor)
output_tensor = input_tensor.moveaxis(0, 2)
print(output_tensor)