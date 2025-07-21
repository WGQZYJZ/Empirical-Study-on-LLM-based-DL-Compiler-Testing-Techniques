'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ceil_\ntorch.Tensor.ceil_(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = torch.ceil(input_tensor)
print(output_tensor)
output_tensor = torch.Tensor.ceil_(input_tensor)
print(output_tensor)
output_tensor = input_tensor.ceil()
print(output_tensor)
output_tensor = input_tensor.ceil_()
print(output_tensor)