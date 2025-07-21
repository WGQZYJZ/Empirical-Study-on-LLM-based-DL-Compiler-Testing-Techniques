'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tensor_split\ntorch.Tensor.tensor_split(_input_tensor, indices_or_sections, dim=0)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print(input_tensor)
indices_or_sections = [2, 2]
output_tensor = input_tensor.tensor_split(indices_or_sections, dim=2)
print(output_tensor)