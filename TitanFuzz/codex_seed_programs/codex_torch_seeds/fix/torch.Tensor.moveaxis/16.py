'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.moveaxis\ntorch.Tensor.moveaxis(_input_tensor, source, destination)\n'
import torch
input_data = torch.randn(2, 3, 4)
print(input_data)
output_data = input_data.moveaxis(0, (- 1))
print(output_data)