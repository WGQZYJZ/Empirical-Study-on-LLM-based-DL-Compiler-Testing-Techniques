'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctan_\ntorch.Tensor.arctan_(_input_tensor)\n'
import torch
input_tensor = torch.rand(1, 3, 3)
print(input_tensor)
output_tensor = input_tensor.arctan_()
print(output_tensor)