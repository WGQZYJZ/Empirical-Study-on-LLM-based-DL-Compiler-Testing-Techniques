'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.moveaxis\ntorch.Tensor.moveaxis(_input_tensor, source, destination)\n'
import torch
input_tensor = torch.randn(2, 3, 5)
print(input_tensor)
output_tensor = torch.Tensor.moveaxis(input_tensor, 0, 1)
print(output_tensor)
output_tensor = torch.Tensor.moveaxis(input_tensor, 1, (- 1))
print(output_tensor)
output_tensor = torch.Tensor.moveaxis(input_tensor, (- 1), 1)
print(output_tensor)