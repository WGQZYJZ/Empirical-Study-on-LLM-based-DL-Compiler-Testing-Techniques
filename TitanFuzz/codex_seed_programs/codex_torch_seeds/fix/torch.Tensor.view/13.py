'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view\ntorch.Tensor.view(_input_tensor, *shape)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor)
output_tensor = input_tensor.view(1, 12)
print(output_tensor)
output_tensor = input_tensor.view(12)
print(output_tensor)
output_tensor = input_tensor.view(4, 3)
print(output_tensor)
output_tensor = input_tensor.view(2, 6)
print(output_tensor)